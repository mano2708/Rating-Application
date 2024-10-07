from django.db import models

# Common choices for ratings
RATING_CHOICES = [
    ('0', 'None'),
    ('1', '⭐'),
    ('2', '⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('5', '⭐⭐⭐⭐⭐')
]

class User(models.Model):

    name = models.CharField(max_length=100, help_text="Enter your name")
    email = models.EmailField(primary_key=True, help_text="Enter your email")

    def __str__(self):
        return self.name


class SecondYear(models.Model):

    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_year_users')

    projects={
              "AUTONEXUS"           :       "AUTONOMOUS VEHICLE",
              "APEXDEV"             :       "PLACEMENT MANAGEMENT SYSTEM",
              "CODE CRACKERS"       :       "WEB BASED WEATHER FORCASTING",
              "INFINITY ERRORS"     :       "OTP GENERATOR",
              "FUTURE DEVELOPERS"   :       "BRAIN TEASERS",
              "SUNFLOWER SYNERGY"   :       "GRADENOTIFIER",
              "GPS CODERS"          :       "ONLINE EXAMINATION MANAGEMENT SYSTEM",
              "TECH TITANS"         :       "INTERACTIVE PORTFOLIO HUB",
              "ETHICAL EAGLES"      :       "ATTENDANCE TRACKER",
              "ERROR LIST"          :       "WEB SCRAPPING",
              "CODE TECHNICIANS"    :       "FITNESS PLAN GENERATOR",
              "NOVA SPIRE"          :       "CONVERTING E-BBOKS TO AUDIOBOOKS",
              "SPARKLING STARS"     :       "TRAVEL CHATBOT",
              "DEADLINE DOMINATORS" :       "DRIVER DROWSINESS DETECTION",
              "TECH SPARK"          :       "BANKING MANAGEMENT SYSTEM",
              "TECHNOZ"             :       "BLOGGING PLATFORM",
              "404 ERROR"           :       "IQ TEST BETWEEN DIFFERENT AGED PEOPLE",
              "CLEVER CODERS"       :       "TRAVEL AND TOURISM MANAGEMENT SYSTEM",
              "TECH TWINS"          :       "TETRIS GAME",
              "SONIC SIRENS"        :       "MUSIC PLAYER",
              "TECHNONGEMS"         :       "WIKIPEDIA SEARCH APPLICATION",
              "CODE SMITHS"         :       "FILE ORGANISER",
              }
    

    # Dynamically create fields for projects
    for project_name,help_text in projects.items():
        locals()[project_name.replace(' ', '_')] = models.CharField(
            max_length=2,
            default='0',
            choices=RATING_CHOICES,
            help_text=help_text
        )

    def __str__(self):
        return self.user.name

class ThirdYear(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='third_year_users')

    projects={
              "ELITE CREW"          :       "RESUME BUILDER",
              "FIN-MENTORS"         :       "SMART GARDEN IRRIGATION SYSTEM",
              "SLC-1"               :       "ECOMMERCE FOOD WEBSITE (USER MODULE)",
              "SLC-2"               :       "ECOMMERCE FOOD WEBSITE (ADMIN MODULE)",
              "404 NOT FOUND"       :       "SPEECH EMOTION RECOGNITION",
              "INNOVATORS"          :       "OUTPASS MANAGEMENT SYSTEM",
              "CODE CRUSHERS"       :       "KNOWLEDGE APTITUDE PREP HUB",
              "TECH NINJAS"         :       "WOMEN SAFETY APPLICATION",
              "NULL CODERS"         :       "KEYLOGGER",
              "NEW YORK SIRENS"     :       "ONLINE AUCTION SYSTEM",
              "TECH TITANS"         :       "CAR RENTAL SYSTEM",
              "FLAMING TRIO'S"      :       "SIMULATION OF RAILWAY PLATFORM TICKET DISPENSING SYSTEM",
              "ROBO RACERS"         :       "BLUETOOTH CONTROLLED AURDINO CAR",
              "LOGIC KILLER"        :       "COMPREHENSIVE PLATFORM FOR QUESTION PAPERS",
              "VERSE VILLAINS"      :       "BOOKWORM UNITE",
              "DEBUT CODERS"        :       "BRIDGING GAPS",
              "STELLAR SQUAD"       :       "WASTE FOOD MANAGEMENT",
              "KODERS"              :       "QUIZ GAME",
              "SMART TECH"          :       "AUTOMATED PLANT DISEASE DETECTION SYSTEM USING DEEP LEARNING",
              "QUARTO"              :       "WEB APPLICATION FOR DIRECT MARKET ACCESS TO FARMERS",
              "TECH WIZARDS"        :       "SALESMAN TRACKING SYSTEM",
              "IT IMMORTALS"        :       "SKILLMATCH PRO",
              }
    

    # Dynamically create fields for projects
    for project_name,help_text in projects.items():
        locals()[project_name.replace(' ', '_')] = models.CharField(
            max_length=2,
            default='0',
            choices=RATING_CHOICES,
            help_text=help_text
        )

    def __str__(self):
        return self.user.name