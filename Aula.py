from pprint import pprint
from classes import *
from db.database import Database
from helper.WriteAJson import writeAJson
from bson.objectid import ObjectId

class ControleAulas:
    def __init__(self):
        self.db = Database(database="faculdade", collection="Aulas")
        self.collection = self.db.collection

    def cria_aula(self, assunto: str, professor: object, alunos: list):
        luc = self.collection.insert_one({

            "assunto": assunto,
            "professor": {
                "nome": getattr(professor, 'nome'),
                "especialidade": getattr(professor, 'especialidade')
            }
        })

        a = len(alunos)
        for i in range(a):
            self.collection.update_one(
                {"_id": luc.inserted_cod}, {"$push": {
                    "alunos": {
                        "nome": getattr(alunos[i], 'nome'),
                        "matricula": getattr(alunos[i], 'matricula'),
                        "curso": getattr(alunos[i], 'curso'),
                        "periodo": getattr(alunos[i], 'periodo')
                    }
                }
            })
        return luc.inserted_cod

    def assunto_up(self, cod: str, assunto: str):
        luc = self.collection.update_one({"_id": ObjectId(cod)}, {"$set": {"assunto": assunto}})
        return luc.modified_count

    def prof_up(self, cod: str, professor: object):
        luc = self.collection.update_one({"_id": ObjectId(cod)}, {"$set": {
            "professor": {
                "nome": getattr(professor, 'nome'),
                "especialidade": getattr(professor, 'especialidade')
            }
        }})
        return luc.modified_count

    def turma_up(self, cod: str, alunos: list):
        self.collection.update_one({"_id": ObjectId(cod)}, {"$set": {"alunos": []}})

        a = len(alunos)
        for i in range(a):
            luc = self.collection.update_one(
                {"_id": ObjectId(cod)}, {"$push": {
                    "alunos": {
                        "nome": getattr(alunos[i], 'nome'),
                        "matricula": getattr(alunos[i], 'matricula'),
                        "curso": getattr(alunos[i], 'curso'),
                        "periodo": getattr(alunos[i], 'periodo')
                    }
                }
            })
        return luc.modified_count

    def aluno_up(self, cod: str, aluno: object):

        luc = self.collection.update_one(
            {"_id": ObjectId(cod)}, {"$push": {
                "alunos": {
                    "nome": getattr(aluno, 'nome'),
                    "matricula": getattr(aluno, 'matricula'),
                    "curso": getattr(aluno, 'curso'),
                    "periodo": getattr(aluno, 'periodo')
                }
            }
        })
        return luc.modified_count

    def aluno_del(self, cod: str, matriculaAluno: str):
        luc = self.collection.update_one(
            {"_id": ObjectId(cod)}, {"$pull": {
                "alunos": {
                    "matricula": matriculaAluno
                }
            }
            })
        return luc.modified_count

    def aula_del(self, cod: str):
        luc = self.collection.delete_one({"_id": ObjectId(cod)})
        return luc.deleted_count

