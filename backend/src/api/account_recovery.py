from fastapi import APIRouter, HTTPException
from src.schemas.user import UserDB, UserModelPublic
from src.schemas.recovery import AccountRecovery, PasswordChangeResponse
from .users import search_user


router = APIRouter()

@router.put(
    "/", status_code=200 , response_model=PasswordChangeResponse, tags=["account recovery"]
)
def change_password(account_recovery: AccountRecovery):
    user = search_user(account_recovery.email) # procura um usuário com email igual ao do formulário
    if not user: # se não encontrar o usuário: erro 404
        raise HTTPException(status_code=404, detail="User not found")
    if account_recovery.new_password == account_recovery.confirm_password: 
        user.passwd = account_recovery.new_password
        return PasswordChangeResponse(email=user.email, new_password=user.passwd)
    else:
        raise HTTPException(status_code=400, detail="Passwords do not match") # se as senhas digitadas forem diferentes: erro 400