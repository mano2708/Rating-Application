# from django.db import models

# # Create your models here.
# class RatingTableOne(models.Model):

#     Name = models.CharField(max_length=15,primary_key=True)
#     rValue=[
#         ('0','None'),('1','⭐'),('2','⭐⭐'),('3','⭐⭐⭐'),('4','⭐⭐⭐⭐'),('5','⭐⭐⭐⭐⭐')
#     ]
#     No_1= models.CharField(max_length=2,default='0',choices=rValue,help_text='Synergic Calculator')
#     No_2 = models.CharField(max_length=2,default='0',choices=rValue,help_text='ID Card Generator')
#     No_3 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Inventory Management')
#     No_4 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Food Chatbot')
#     No_5 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Incident Reporter')
#     No_6 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Banking System')
#     No_7 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Voting System')
#     No_8 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Bus Times')
#     No_9 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Secret Code')
#     No_10 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Health Dot')
#     No_11 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Online Attendance using Face Recognition')
#     No_12 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Heart Disease Prediction')
#     No_13 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Exquisite Checks')
#     No_14 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Facemask Detection System')
#     No_15 = models.CharField(max_length=2,default='0',choices=rValue,help_text='OTP Verification')
#     No_16 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Language Translator')
#     No_17= models.CharField(max_length=2,default='0',choices=rValue,help_text='Matrix Calculator')
#     No_18 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Project Info')
#     No_19 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Housing Society Management System')
#     No_20 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Hangman')
#     No_21 = models.CharField(max_length=2,default='0',choices=rValue,help_text="Virtual Counselor")





# class RatingTableTwo(models.Model):
#     Name = models.CharField(max_length=15,primary_key=True)
#     rValue=[
#         ('0','None'),('1','⭐'),('2','⭐⭐'),('3','⭐⭐⭐'),('4','⭐⭐⭐⭐'),('5','⭐⭐⭐⭐⭐')
#     ]
#     No_1= models.CharField(max_length=2,default='0',choices=rValue,help_text='Interview IQ:Aptitude&Interview Training Game')
#     No_2 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Steganography')
#     No_3 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Controlling Home Appliances using Voice Assistence')
#     No_4 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Virtual AI Assistent')
#     No_5 = models.CharField(max_length=2,default='0',choices=rValue,help_text='IV Bag Monitoring & Alert System')
#     No_6 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Virtual Mouse')
#     No_7 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Barrier Buster')
#     No_8 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Object Detection')
#     No_9 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Fraud Detection')
#     No_10 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Gesture Control')
#     No_11 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Plagiarism Checker')
#     No_12 = models.CharField(max_length=2,default='0',choices=rValue,help_text='E-Cart Universe & AI Virtual Marker')
#     No_13 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Word Game')
#     No_14 = models.CharField(max_length=2,default='0',choices=rValue,help_text='Song Recommendation using Face Reaction')


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

    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.name


class SecondYear(models.Model):

    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_year_users')

    projects={"ETHICAL EAGLES":"ATTENDANCE TRACKER",
              "SUNFLOWER SYNERGY":"GRADENOTIFIER",
              "GRADENOTIFIER":"AUTONOMOUS VEHICLE",
              "SONIC SIRENS":"MUSIC PLAYER",
              "MUSIC PLAYER":"DRIVER DROWSINESS DETECTION",
              "TECH SPARK":"BANKING MANAGEMENT SYSTEM",
              "404 ERROR":"IQ TEST BETWEEN DIFFERENT AGED PEOPLE",
              "APEXDEV":"PLACEMENT MANAGEMENT SYSTEM",
              "TECH TWINS":"TETRIS GAME",
              "SPARKLING STARS":"TRAVEL CHATBOT",
              "CLEVER CODERS":"TRAVEL AND TOURISM MANAGEMENT SYSTEM",
              "TRAVEL AND TOURISM MANAGEMENT SYSTEM":"WIKIPEDIA SEARCH APPLICATION",
              "GPS CODERS":"ONLINE EXAMINATION MANAGEMENT SYSTEM",
              "CODE SMITHS":"FILE ORGANISER",
              "TECHNOZ":"BLOGGING PLATFORM",
              "TECH TITANS":"INTERACTIVE PORTFOLIO HUB",
              "ERROR LIST":"WEB SCRAPPING",
              "CODE TECHNICIANS":"FITNESS PLAN GENERATOR",
              "FUTURE DEVELOPERS":"BRAIN TEASERS",
              "INFINITY ERRORS":"OTP GENERATOR"}
    

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

    projects={"SLC-1":"ECOMMERCE FOOD WEBSITE (USER MODULE)",
              "SLC-2":"ECOMMERCE FOOD WEBSITE (ADMIN MODULE)",
              "404 NOT FOUND":"SPEECH EMOTION RECOGNITION",
              "LOGIC KILLER":"COMPREHENSIVE PLATFORM FOR QUESTION PAPERS",
              "IT IMMORTALS":"SKILLMATCH PRO",
              "TECH NINJAS":"WOMEN SAFETY APPLICATION",
              "DEBUT CODERS":"BRIDGING GAPS",
              "QUARTO":"WEB APPLICATION FOR DIRECT MARKET ACCESS TO FARMERS",
              "STELLAR SQUAD":"WASTE FOOD MANAGEMENT",
              "INNOVATORS":"OUTPASS MANAGEMENT SYSTEM",
              "VERSE VILLAINS":"BOOKWORM UNITE",
              "TECH TITANS":"CAR RENTAL SYSTEM",
              "NEW YORK SIRENS":"ONLINE AUCTION SYSTEM",
              "NULL CODERS":"KEYLOGGER",
              "FLAMING TRIO'S":"SIMULATION OF RAILWAY PLATFORM TICKET DISPENSING SYSTEM",
              "ELITE CREW":"RESUME BUILDER",
              "ROBO RACERS":"BLUETOOTH CONTROLLED AURDINO CAR",
              "SMART TECH":"AUTOMATED PLANT DISEASE DETECTION SYSTEM USING DEEP LEARNING",
              "FIN-MENTORS":"SMART GARDEN IRRIGATION SYSTEM",
              "KODERS":"QUIZ GAME",
              "TECH WIZARDS":"SALESMAN TRACKING SYSTEM",
              "CODE CRUSHERS":"KNOWLEDGE APTITUDE PREP HUB"
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