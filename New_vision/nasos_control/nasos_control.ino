#include <Wire.h> 
#include <LiquidCrystal_I2C.h>


//int PotenciometrPin = A0;    // select the input pin for the potentiometer
//int Value=0;
//float Value_volt=0;
LiquidCrystal_I2C lcd(0x27,16,2);  // Устанавливаем дисплей
//  lcd.init();                     
//  lcd.backlight();// Включаем подсветку дисплея
//  lcd.print("iarduino.ru");
//  lcd.setCursor(4, 1);
//  lcd.print("Potenciometr");
//   delay(1000);

int downPin1 = 2; // к выводу 2 подключён геркон 1
int upPin2 = 3; // к выводу 3 подключён геркон 2
int alarmPin3 = 4; // к выводу 4 подключён геркон 3
int ledPin = 13;
int flag = 0;

String str1 = "gerkon_down= ";
String str2 = "gerkon_up= ";
String str3 = "gerkon_alarm= ";
int relay1_on_off = 5; // к выводу 5 подключено реле 1 
int relay2 = 6; // к выводу 6 подключено реле 2
int relay3_alarm = 7; // к выводу 7 подключено реле 3 
int tempSensor = A0;
float  Value_volt=0;
float gradus=0;
int led_light = 0;
void setup() {
  lcd.init();                      // initialize the lcd 
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  Serial.begin(9600); // задействуем последовательный порт
  
  pinMode(downPin1, INPUT); // задаём вывод 2 в качестве входа (будем считывать с него)
  pinMode(upPin2, INPUT); // задаём вывод 3 в качестве входа (будем считывать с него)
  pinMode(alarmPin3, INPUT); // задаём вывод 4 в качестве входа (будем считывать с него)
  digitalWrite(downPin1, HIGH); // активируем внутренний подтягивающий резистор вывода
  digitalWrite(upPin2, HIGH); // активируем внутренний подтягивающий резистор вывода
  digitalWrite(alarmPin3, HIGH); // активируем внутренний подтягивающий резистор вывода
  
  pinMode(relay1_on_off, OUTPUT);  // D5 как выход
  pinMode(relay2, OUTPUT);  // D6 как выход
  pinMode(relay3_alarm, OUTPUT);  // D7 как выход
  
  pinMode(ledPin, OUTPUT); // задаём вывод 13 в качестве выхода
  pinMode (tempSensor, INPUT);   
}

void loop() {
  
  int g1 = digitalRead(downPin1); // считываем показания с геркона
  int g2 = digitalRead(upPin2); // считываем показания с геркона
  int g3 = digitalRead(alarmPin3); // считываем показания с геркона
  g1 = !g1; 
  g2 = !g2;
  g3 = !g3;
  
//  Serial.println(g1);
  digitalWrite(ledPin, led_light); // инвертированные показания записываем в порт со светодиодом
  led_light = !led_light;
  Serial.println(str1 + g1); // посылаем в последовательный порт значения с геркона
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)
  Serial.println(str2 + g2); // посылаем в последовательный порт значения с геркона
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)
  Serial.println(str3 + g3); // посылаем в последовательный порт значения с геркона
  //когда геркон замкнут, значение "1" (HIGH), когда разомкнут - "0" (LOW)
//   int val = analogRead(tempSensor);
//   Serial.println(val);
//   Value_volt=(float)5/1024*val;
//   Serial.println(Value_volt);
//   gradus = (float)5/1024*val*10/0.71;
//   Serial.println(gradus);
   
   
   
   if (g1==1&&g2==1&&g3==1)//вкл вкл вкл 
    {Serial.println("status= 1.1.1 ALARM!!!");
    lcd.clear();
    lcd.print("1.1.1 ALARM!!!");
   
     digitalWrite(relay3_alarm, 0);
     digitalWrite(relay1_on_off, 0);
     flag = 1;
    }
    else if (g1==1&&g2==1&&g3==0)//вкл вкл выкл
    {Serial.println("status= 1.1.0 ALARM!!!");
    lcd.clear();
    lcd.print("1.1.0 ALARM!!!");
    
     digitalWrite(relay3_alarm, 0);
     digitalWrite(relay1_on_off, 0);
     flag = 1;
    }
    else if (g1==0&&g2==0&&g3==1)// выкл выкл вкл 
    {Serial.println("status= 0.0.1 ALARM!!!");
    lcd.clear();
    lcd.print("0.0.1 ALARM!!!");
  
     digitalWrite(relay3_alarm, 0);
     digitalWrite(relay1_on_off, 0);
     flag = 1;
    }
    else if (g1==0&&g2==1&&g3==1)// выкл вкл вкл 
    {Serial.println("status= 0.1.1 ALARM!!!");
    lcd.clear();
    lcd.print("0.1.1 ALARM!!!");

     digitalWrite(relay3_alarm, 0);
     digitalWrite(relay1_on_off, 0);
     flag = 1;
    }
     else if (g1==1&&g2==0&&g3==1)//вкл выкл вкл 
    {Serial.println("status= 1.0.1 ALARM!!!");
    lcd.clear();
    lcd.print("1.0.1 ALARM!!!");

     digitalWrite(relay3_alarm, 0);
     digitalWrite(relay1_on_off, 0);
     flag = 1;
    }
    else if(g1==1&&g2==0&&g3==0) //набор воды
    {digitalWrite(relay3_alarm, 1);
     delay(300);
     digitalWrite(relay1_on_off, 1);
     delay(300);
     Serial.println("status= Intake has begun, level low");
     lcd.clear();
     lcd.print("Intake has begun");

     
     flag = 3;
    }
   else if(g1==0&&g2==1&&g3==0)//окончание набора воды
    {digitalWrite(relay3_alarm, 0);
     delay(300);
     digitalWrite(relay1_on_off, 0);
     delay(300);
     Serial.println("status= Intake is over, level high");
     lcd.clear();
     lcd.print("Intake is over");
     
    flag = 4;
    }
   else if(g1==0&&g2==0&&g3==0)//неизвестная позиция
    {if(flag==0){Serial.println("status= Status temporarily unknown");
    lcd.clear();
    lcd.print("temporarily unknown");
   }
     else if(flag==1){Serial.println("status= flag1 ALARM!!!");
     lcd.clear();
     lcd.print("flag1 ALARM!!!");
     }
     else if(flag==3){Serial.println("status= flag3 Intake has begun");
     lcd.clear();
     lcd.print("3 Intake has begun");
     }
     else if(flag==4){Serial.println("status= flag4 Intake is over");
     lcd.clear();
     lcd.print("4 Intake is over");
   }
     else{Serial.println("status= Status be updated by flag");
     lcd.clear();
     lcd.print("updated by flag");
   }
    }
    Serial.println("Position relay1_on_off= " + String(digitalRead(relay1_on_off)));
    Serial.println("Position relay2= " + String(digitalRead(relay2)));
    Serial.println("Position relay3_alarm= " + String(digitalRead(relay3_alarm)));
//   Serial.println(flag);

//   Serial.println("\n№ аналогового вывода\t'Сырые данные'\tПроценты");
//
//  Serial.println("------------------------------------------------");
//
//  for (int i = 0; i < 10; i++)
//  {
//    int val = analogRead(POT);                        // Читаем значения с потенциометра
//    int per = map(val, 0, 1023, 0, 100);              // Конвертируем в проценты
//   
//    Serial.print("A0\t\t\t");
//    Serial.print(val);                                // Выводим на печать в последовательный порт необработанные("сырые") аналоговые значения
//    Serial.print("\t\t");     
//    Serial.print(per);                                // Выводим на печать в последовательный порт значения в процентах
//    Serial.println("%");                              // Выводим на печать в последовательный порт символ % и новой строки
//  }

//  lcd.setCursor(0, 0);
//  lcd.print("     - ____V    ");  // Устанавливаем курсор на вторую строку и нулевой символ.
//  lcd.setCursor(0, 1);  // Выводим на экран значение с аналогового входа (от 0 до 1024 пропорционально от 0 В. до 5 В.)
//  Value = analogRead(PotenciometrPin);    
//  lcd.print(Value);
//  lcd.setCursor(7, 1);
//  Value_volt = (float)5/1024*Value;
//  lcd.print(Value_volt);
//  Serial.println(Value_volt);

  
  delay(1000); // повторяем цикл через 1000 мсек
}
