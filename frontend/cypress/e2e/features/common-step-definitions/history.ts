import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

//Scenario: Consulta do Historico Geral
  //Given o usuário de id "1" está logado -> Ja implementado
  //And o usuário está na página "history" -> Ja implementado
  //When o usuário clica em "Todos"
  When("o usuário clica em {string}", (button: string) => {
    cy.getDataCy(button).click();
});
  //Then é exibido uma lista de "Videos" com "Barbie"
   Then("é exibido uma lista de {string} com {string}", (field:string, message: string) => {
    cy.getDataCy(field).should('contain', message);
});

Then("é exibido uma lista de {string} com {string} e {string}", (field:string, video1: string, video2:string) => {
  cy.getDataCy(field).should('contain', video1);
  cy.getDataCy(field).should('contain', video2);
});