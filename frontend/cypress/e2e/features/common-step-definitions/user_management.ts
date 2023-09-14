import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import axios from 'axios';


// Scenario: Cadastro bem sucedido de um usuário

// Given: login.ts
// When: login.ts
// And: login.ts
// Then: login.ts    


// Scenario: Exclusão de conta

//   Given o usuário de id "1" está logado
Given("o usuário de id {string} está logado", (id: string) => {
    localStorage.setItem("token", id) 
});

Then("o usuário é direcionado para a pagina {string}", (page: string) => {
    localStorage.removeItem("token");
    cy.url().should('include', page);
});
//   Given o usuário está na página "account-management"
//   When eu seleciono "deletar conta"
//   And eu seleciono "confirmar"
//   Then na tela "login" eu recebo a mensagem "conta deletada"



// Scenario: e-mail não cadastrado no sistema

// Given: login.ts
// When: login.ts
// When: login.ts

// Scenario: senha incorreta

// Given: login.ts
// When: login.ts
// When: login.ts
// Then: login.ts
// Then: login.ts
