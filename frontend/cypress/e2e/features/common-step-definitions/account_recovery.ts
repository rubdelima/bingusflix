import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

// Scenario: usuário solicita recuperação de conta

// Given: login.ts

When("o usuário clica no botão {string}", (button: string) => {
    cy.getDataCy(button).click();
});

Then("o usuário é direcionado para a página {string}", (page: string) => {
    cy.url().should('include', page);
});

// Scenario: usuário altera sua senha por meio da recuperação de conta

// Given: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
// When: login.ts

Then("o usuário recebe a mensagem de confirmação {string}", (message: string) => {
    cy.getDataCy('success-message').should('contain', message);
});

// Scenario: e-mail inválido na recuperação de conta

// Given: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
// Then: login.ts

// Scenario: confirmação de senha diferente da nova senha

// Given: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
// When: login.ts
