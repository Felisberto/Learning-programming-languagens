/*
Faça um programa para calcular o valor de uma viagem.

Você terá 3 variáveis. Sendo elas:
 1 - Preço do combustível;
 2 - Gasto médio de combustível do carro por KM;
 3 - Distância em KM da viagem;

Imprima no console o valor que será gasto para realizar esta viagem.*/
const co_pric = 5.49;
const gasto_med = 0.45; // 1 litro a cada 12 km em (5.49/12(km)=0.45 em média)
var dist_km = window.prompt("Quantos KM terá a viagem?");
var total = 0
document.write(`Com o preço da gasolina a ${co_pric} e uma média de gasto por km de ${gasto_med} e com uma distância de ${dist_km} Km.<br/>`);
document.write(`O valor total da viagem é de ${(total = (dist_km * co_pric) / gasto_med).toFixed(2)} reais.`);
console.log(total.toFixed(2), "reais");
