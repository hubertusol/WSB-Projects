function zadanie_1() {
    console.log("Witaj Swiecie!");
  }
  function zadanie_2(){
   var imie=Hubert;
   console.log(imie);
  }
  function zadanie_3(){
    var liczba = 127;
    var kwadrat = liczba*liczba;
    return kwadrat;
    document.write(kwadrat);
  }
  function zadanie_4(){
    for(var i=0;i<10;i++){
      console.log(i+1);
    }
  }
  function zadanie_5(x,y){
    return x+y;
  }
  function zadanie_6(a,b,c){
    var liczby = [a,b,c];
    var najwieksza = a;
    for(i=0;i<9;i++){
      try{
        if(liczby[i]>liczby[i-1]){
        najwieksza=liczby[i];
      }
        else if(liczby[i]<liczby[i-1]){
          najwieksza=liczby[i-1];
        }
      } catch(error){continue;}
    }
    console.log(najwieksza);
    return najwieksza;
  }
  //Zadania 7 i 8
  var tablica = [1,2,3,4,5];
  function zadanie_7(){
      console.log(tablica);
  }
  function zadanie_8(){
      for(i=0;i<tablica.length;i++){
          document.write(tablica[i]);
      }
  }
  //Zadania 9 i 10
  var obiekt = {
          imie:"Hubert",
          nazwisko:"Sołtys",
          wiek:20
      };
  function zadanie_9(){
      console.log(obiekt);
  }
  function zadanie_10(){
      obiekt.hobby = ["Gry","Samochody","Dziewczyny"];
      console.log(obiekt);
  }
  //Zadania 11 i 12
  liczby = [0.001,0.01,0.1,1,10,100];
  function zadanie_11(x){
      var wynik=0;
      for(var i=0;i<x.length;i++){
          wynik+=x[i];
      }
      console.log(wynik);
  }
  function zadanie_12(x){
      var suma=0;
      var srednia=0;
      for(var i=0;i<x.length;i++){
          suma+=x[i];
      }
  }