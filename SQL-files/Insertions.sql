
INSERT INTO students (SocialSecurityNumber,FirstName,LastName,Email,PhoneNumber)
VALUES
  ("01-01-02-0000","Susan","Mckee","ultrices.posuere@google.couk","07813-468752"),
  ("02-01-02-0000","Damon","Head","tempor.bibendum@yahoo.couk","0855-772-8727"),
  ("03-01-02-0000","Norman"," Deleon","nunc.lectus.pede@outlook.ca","0845-46-41"),
  ("04-01-02-0000","Wyatt","Carr","pellentesque.habitant@protonmail.couk","055-3255-5526"),
  ("05-01-02-0000","Yoko","Burgess","ac.mattis@yahoo.org","0800-254-4021"),
  ("06-01-02-0000","Elton","Ward","sed.eu@icloud.net","055-0815-7380"),
  ("07-01-02-0000","Aileen","Hicks","lacus.pede.sagittis@yahoo.net","076-5315-1285"),
  ("08-01-02-0000","Odette","Armstrong","tincidunt.pede@aol.couk","0398-154-8763"),
  ("09-01-02-0000","Dillon","Maynard","ante.blandit@google.couk","07624-027814"),
  ("10-01-02-0000","Diana","Burch","eu@yahoo.net","0500-939432");
SELECT * FROM students;
INSERT INTO types(Name,Description)
VALUES
	("VR Headset","headsets used to play VR-games or use for VR related things"),
	("Game","Games which can be borrowed from the lab"),
	("Microcontroller","A small computer, on a single circuit.");
SELECT * FROM types;
INSERT INTO equipment(Name,TypeId,Description,TotalNumberItems)
VALUES
("Valve Index",1,"The Valve Index is a consumer virtual reality headset created and manufactured by Valve.",1),
("Occulus Quest",1,"A consumer virtual reality headset developed by Meta.",1),
("Chess set",2,"A set for playing chess",5),
("Chessex Dice set",2,"A dice set consisting of d20s,d12s,d8s and so on",2),
("Rasberry PI 4 4gb",3,"A small general purpose computer used to develop all kinds of things",18);

INSERT INTO bookings(SocialSecurityNumber,EquipmentId,NumberOfItems,StartDate,EndDate)
VALUES 
("01-01-02-0000",1,1,"2023-05-01","2023-05-08"),
("01-01-02-0000",1,1,"2024-01-01","2023-01-20"),
("02-01-02-0000",1,1,"2023-05-01","2023-05-08"),
("02-01-02-0000",1,1,"2023-05-01","2023-05-08"),
