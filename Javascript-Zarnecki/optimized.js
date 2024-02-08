// Zadanie 1
console.log("Zadanie 1:");
console.log("Witaj Swiecie!");

// Zadanie 2
console.log("Zadanie 2:");
var imie="Hubert";
console.log(imie);

// Zadanie 3
console.log("Zadanie 3:");
  var liczba = 12;
  var kwadrat = liczba * liczba;
  console.log(kwadrat)
  //document.write(kwadrat);

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
console.log(zadanie_5(2, 3));

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
  return najwieksza;
}
console.log(zadanie_6(5, 10, 8));

// Zadanie 7
console.log("Zadanie 7:");
var tablica = [1, 2, 3, 4, 5];
console.log(tablica);

// Zadanie 8
console.log("Zadanie 8:");
function zadanie_8() {
  for (var i = 0; i < tablica.length; i++) {
    console.log(tablica[i])
    //document.write(tablica[i]);
  }
}
zadanie_8();

// Zadanie 9
console.log("Zadanie 9:");
var obiekt = { 
imie: "Hubert",
nazwisko: "Sołtys",
wiek: 20}
console.log(obiekt);

// Zadanie 10
console.log("Zadanie 10:");
  obiekt.hobby = ["Gry", "Samochody", "Dziewczyny"];
  console.log(obiekt);

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
tablica_mieszana = [1,1,'b',0,'a','a',3,'d',4,'c',4,1,'a'];
function zadanie_17(tab){
    for(i=1;i<=tab.length;i++){
        console.log(tab[tab.length-i]);
    }
}
zadanie_17(tablica_mieszana);

// Zadanie 18
console.log("Zadanie 18:");
function zadanie_18(tab){
    return tab.sort();
}
console.log(zadanie_18(tablica_mieszana));

// Zadanie 19
console.log("Zadanie 19:");
function zadanie_19(tab){
    tab.sort();
    tab.reverse();
    return tab;
}
console.log(zadanie_19(tablica_mieszana));

// Zadanie 20
console.log("Zadanie 20:");
function zadanie_20(tab){
    for(i=0;i<tab.length;i++){
        for(x=0;x<tab.length-1;x++){
            if(i==x){continue;}
            if(tab[i]==tab[x]){
                delete tab[x];
            }
        }
    }
    return tab.filter(n => n !== null && n !== undefined && n !== '');
}
console.log(zadanie_20(tablica_mieszana));

// Zadanie 21
console.log("Zadanie 21:");
function zadanie_21(slowo_1,slowo_2){
    if(slowo_1==slowo_2){return true;}
    else{return false;}
}
console.log(zadanie_21("AlaMaKota","AlaMaKota"));
console.log(zadanie_21("AlaMaKota","KotMaAle"));

// Zadanie 22
console.log("Zadanie 22:");
function zadanie_22(slowo){
   return slowo.length;
}
console.log(zadanie_22("LubieProgramowac"));

// Zadanie 23
console.log("Zadanie 23:");
function zadanie_23(slowo){
   return slowo[0];
}
console.log(zadanie_23("MałeCoNieCo"));

// Zadanie 24
console.log("Zadanie 24:");
function zadanie_24(slowo){
    var tablica_temp=[];
    tablica_temp=slowo.split('');
    tablica_temp.reverse();
    slowo=tablica_temp.join('')
    return slowo;
}
console.log(zadanie_24("Technikum"));

// Zadanie 25
console.log("Zadanie 25:");
function zadanie_25(slowo_1,slowo_2){
    return slowo_1.includes(slowo_2);
}    
console.log(zadanie_25("AlaMaKota","Ala"));
console.log(zadanie_25("Ziktor","Wiertara"));

// Zadanie 26
console.log("Zadanie 26:");
function zadanie_26(slowo){
    return slowo.replace(/ /g, '');
}    
console.log(zadanie_26("Ala Ma Kota, Bardzo Ładnego."));

// Zadanie 27
console.log("Zadanie 27:");
function zadanie_27(slowo){
    return slowo.toLowerCase()
}    
console.log(zadanie_27("Ala Ma Kota, Bardzo Ładnego."));

// Zadanie 28
console.log("Zadanie 28:");
function zadanie_28(slowo){
    return slowo.toUpperCase()
}    
console.log(zadanie_28("Ala Ma Kota, Bardzo Ładnego."));

// Zadanie 29
console.log("Zadanie 29:");
function zadanie_29(){
    return Date.now()
}    
console.log(zadanie_29());

// Zadanie 30
console.log("Zadanie 30:");
function zadanie_30(){
    const data=new Date();
    wynik = ""+data.getDate()+"."+(data.getMonth()+1)+"."+data.getFullYear();
    return wynik;
}    
console.log(zadanie_30());

// Zadanie 31
console.log("Zadanie 31:");
function zadanie_31(data_1,data_2){
    const roznicaMS = Math.abs(data_1 - data_2); 
    const roznicaGodzin = roznicaMS / (1000 * 60 * 60); 
    console.log("Różnica od godziny napisania kodu i uruchomienia go wynosi: ")
    return roznicaGodzin;
}
data_start = new Date('2024-02-08T17:13:00');
data_end = new Date();
console.log(zadanie_31(data_end,data_start));







