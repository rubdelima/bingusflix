import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import axios from 'axios';
// Scenario: login bem sucedido de um usuário

Given("o usuário está na página {string}", (page: string) => {
    cy.visit(page);
  });

When("o usuário preenche o campo de {string} com {string}", (field: string, value: string) => {
    cy.getDataCy(field).type(value);
});

When("preenche o campo de {string} com {string}", (field: string, value: string) => {
    cy.getDataCy(field).type(value);
});


When("clica no botão {string}", (button: string) => {
    cy.getDataCy(button).click();
});

Then("o usuário é direcionado para a {string}", (page: string) => {
    cy.url().should('include', page);
});

// Scenario: e-mail não cadastrado no sistema

// Given: login.ts
// When: login.ts
// When: login.ts

Then("o usuário recebe a mensagem de erro {string}", (message: string) => {
    cy.getDataCy('error-message').should('contain', message);
});

Then("o usuário continua na página {string}", (page: string) => {
    cy.url().should('include', page);
});

// Scenario: senha incorreta

// Given: login.ts
// When: login.ts
// When: login.ts
// Then: login.ts
// Then: login.ts
