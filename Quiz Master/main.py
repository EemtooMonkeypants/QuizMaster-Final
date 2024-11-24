import pgzrun
TITLE = 'QuizMaster'
WIDTH = 870
HEIGHT = 650
question = []
questionfilename = 'questions.txt'
questioncount = 0
questionindex = 0
score = 0
is_game_over = False
time_left = 10

mbox = Rect(0, 0, 880, 80)
qbox = Rect(0, 0, 650, 150)
tbox = Rect(0, 0, 150, 150)
abox1 = Rect(0, 0, 300, 150)
abox2 = Rect(0, 0, 300, 150)
abox3 = Rect(0, 0, 300, 150)
abox4 = Rect(0, 0, 300, 150)
sbox = Rect(0, 0, 150, 330)

mbox.move_ip(0, 0)
qbox.move_ip(20,100)
tbox.move_ip(700, 100)
abox1.move_ip(20, 270)
abox2.move_ip(370,270)
abox3.move_ip(20, 450)
abox4.move_ip(370, 450)
sbox.move_ip(700, 270)

answerboxes = [abox1, abox2, abox3, abox4]

def draw():
   
   screen.fill('black')
   screen.draw.filled_rect(mbox, 'blue')
   screen.draw.filled_rect(qbox, 'green')
   screen.draw.filled_rect(tbox, 'purple')
   screen.draw.filled_rect(sbox, 'orange')

   for box in answerboxes:
      screen.draw.filled_rect(box, 'red')

   screen.draw.textbox(str(time_left), tbox, color = 'white')
   screen.draw.textbox('skip', sbox, color = 'white', angle = -90)
   screen.draw.textbox('Welcome to Quiz Master!', mbox, color = 'white')
   if len(qu) >0:
      screen.draw.textbox(qu[0], qbox, color = 'white')
      for i, box in enumerate(answerboxes, start=1):
         if i<len(qu):
            screen.draw.textbox(qu[i], box, color = 'white')


   #index = 1
   #for box in answerboxes:
     # screen.draw.textbox(qu[index], box, color = 'white')
      #index +=1

def update():
   movemessage()

def movemessage():
   mbox.x = mbox.x-2
   if mbox.right <0:
      mbox.left = WIDTH

def readquestion():
   global questioncount, question
   qfile = open(questionfilename, 'r')
   for questions in qfile:
      question.append(questions)
      questioncount +=1
   qfile.close()

def readnextquestion():
   global questionindex
   questionindex += 1
   return question.pop(0).split(',')
   

def on_mouse_down(pos):
   index = 1
   for box in answerboxes:
      if box.collidepoint(pos):
         if index is int(qu[5]):
            correct_answer()
         else:
            game_over()
      index +=1
   if sbox.collidepoint(pos):
      skip_question()

def correct_answer():
   global score, qu, question, time_left
   score +=1
   if question:
      qu = readnextquestion()
      time_left = 10
   else:
      game_over()

def skip_question():
   global qu, question, time_left
   if not is_game_over and question:
      qu = readnextquestion()
      time_left = 10
   else:
      game_over()

def game_over():
   global qu, is_game_over, question, time_left
   message = f'Game Over! You got {score} questions correct!'
   qu = [message, '-','-','-','-',5]
   time_left = 0
   is_game_over = True

def update_timer():
   global time_left
   if time_left:
      time_left = time_left-1
   else:
      game_over()

readquestion()
qu = readnextquestion()
clock.schedule_interval(update_timer,1)
pgzrun.go()