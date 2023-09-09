from pydantic import BaseModel, EmailStr

class AccountRecovery(BaseModel): # modelando a recuperação de senha
    email: EmailStr = "user@email.com"
    new_password: str = "new password"
    confirm_password: str = "confirm password"

class PasswordChangeResponse(BaseModel):
    email: EmailStr
    new_password: str
