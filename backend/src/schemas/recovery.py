from pydantic import BaseModel, EmailStr

class AccountRecovery(BaseModel): # modelando a recuperação de senha
    email: EmailStr = "user@example.com"
    new_password: str = "nova senha"
    confirm_password: str = "confirmar senha"