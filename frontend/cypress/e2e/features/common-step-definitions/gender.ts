import {Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";

// Scenario: Acessar a página de um gênero

Given("o usuário de id {string} está logado", (id: string) => {
    localStorage.setItem("token", id)
});

// Given: login.ts

// When: login.ts

// When: login.ts

// Then: login.ts