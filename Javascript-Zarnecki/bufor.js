// Zadanie 1
console.log("Zadanie 1:");
function zadanie_1() {
  console.log("Witaj Swiecie!");
}
zadanie_1();

// Zadanie 2
console.log("Zadanie 2:");
function zadanie_2() {
 var imie="Hubert";
 console.log(imie);
}
zadanie_2();

// Zadanie 3
console.log("Zadanie 3:");
function zadanie_3() {
  var liczba = 127;
  var kwadrat = liczba * liczba;
  return kwadrat;
  document.write(kwadrat);
}
zadanie_3();

// Zadanie 4
console.log("Zadanie 4:");
function zadanie_4() {
  for(var i = 0; i < 10; i++) {
    console.log(i + 1);
  }
}
zadanie_4();

// Zadanie 5
console.log("Zadanie 5:");
function zadanie_5(x, y) {
  return x + y;
}
zadanie_5(2, 3);

// Zadanie 6
console.log("Zadanie 6:");
function zadanie_6(a, b, c) {
  var liczby = [a, b, c];
  var najwieksza = a;
  for(var i = 0; i < 9; i++) {
    try {
      if (liczby[i] > liczby[i - 1]) {
        najwieksza = liczby[i];
      }
      else if (liczby[i] < liczby[i - 1]) {
        najwieksza = liczby[i - 1];
      }
    } catch (error) {
      continue;
    }
  }
  console.log(najwieksza);
  return najwieksza;
}
zadanie_6(5, 10, 8);

// Zadanie 7
console.log("Zadanie 7:");
var tablica = [1, 2, 3, 4, 5];
function zadanie_7() {
  console.log(tablica);
}
zadanie_7();

// Zadanie 8
console.log("Zadanie 8:");
function zadanie_8() {
  for (var i = 0; i < tablica.length; i++) {
    document.write(tablica[i]);
  }
}
zadanie_8();

// Zadanie 9
console.log("Zadanie 9:");
//Obiekt globalny do zadan 9 i 10
var obiekt = { 
  imie: "Hubert",
  nazwisko: "Sołtys",
  wiek: 20
};
function zadanie_9() {
  console.log(obiekt);
}
zadanie_9();

// Zadanie 10
console.log("Zadanie 10:");
function zadanie_10() {
  obiekt.hobby = ["Gry", "Samochody", "Dziewczyny"];
  console.log(obiekt);
}
zadanie_10();

// Zadanie 11
console.log("Zadanie 11:");
//Obiekt globalny do zadan 11 i 12
var liczby = [0.001, 0.01, 0.1, 1, 10, 100];
function zadanie_11(tab) {
  var wynik = 0;
  for (var i = 0; i < tab.length; i++) {
    wynik += tab[i];
  }
  console.log(wynik);
}
zadanie_11(liczby);

// Zadanie 12
console.log("Zadanie 12:");
function zadanie_12(tab) {
  var suma = 0;
  var srednia = 0;
  for (var i = 0; i < tab.length; i++) {
    suma += tab[i];
  }
  console.log(suma / tab.length);
}
zadanie_12(liczby);

// Zadanie 13
console.log("Zadanie 13:");
function zadanie_13(a, b) {
  console.log(a * b);
  return a * b;
}
zadanie_13(2, 3);

// Zadanie 14
console.log("Zadanie 14:");
function zadanie_14(x) {
  var pierwiastek = Math.sqrt(x);
  return pierwiastek;
}
console.log(zadanie_14(25));

// Zadanie 15
console.log("Zadanie 15:");
// Tablica globalna dla zadań 15 i 16
tablica_liczb = [9,5,1,3,4,6,8,7,0];
function zadanie_15(tab){
    var tablica_kwadraty = []
    for(i=0;i<tab.length;i++){
        var kwadrat = tab[i]^2;
        tablica_kwadraty.push(kwadrat);
    }
    return tablica_kwadraty;
}
console.log(zadanie_15(tablica_liczb));

// Zadanie 16
console.log("Zadanie 16:");
function zadanie_16(tab){
    var tablica_potegi= [];
    for(var i=0;i<tab.length;i++){
        var potega = tab[i]^3;
        tablica_potegi.push(potega);
    }
    return tablica_potegi;
}
console.log(zadanie_16(tablica_liczb));

// Zadanie 17
console.log("Zadanie 17:");
// Tablica globalna dla zadan 17,18,19,20
tablica_mieszana = [1,1,'b',0,'a','a',3,'d',4,'c',4];
function zadanie_17(tab){
    for(i=1;i<=tab.length;i++){
        console.log(tab[tab.length-i]);
    }
}
zadanie_17(tablica_mieszana);

// Zadanie 18
console.log("Zadanie 18:");
function zadanie_18(tab){
    return tablica_miesznana.sort();
}
console.log(zadanie_18(tablica_mieszana));


















