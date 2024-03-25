# ##################################################################################################

# #Charachters #####################################################################################

# define narrator = Character("")

# define eza = Character("Eza")

# define khushboo = Character("Khushboo")

# define angus = Character("Angus")

# define imen = Character("Imen")

# define drMyanhardt = Character("Dr. Myanhardt")

# define celina = Character("Dr. Berg")

# #Regular Points ##################################################################################

# default academic_points = 100
# default will_to_survive_points = 100
# default relationship_points = 100 

# #Special Points ###################################################################################
  
# default goodness_points = 0
# default severity_points = 0

# #Booleans ########################################################################################

# default met_imen = False
# default has_tutor = False
# default went_to_office_hours = False

# ##################################################################################################


# label start:

#     jump intro

#     ##############################################################################################
#     #intro
#     ##############################################################################################
#     label intro:

#         scene summer with dissolve 
    
#         narrator "Summer has come to an end, and Eza is preparing to start her first year at the University of Tokyo."

#         narrator "In a spur of the moment decision over the summer, Eza decided to transfer from the business\
#         program into computer science."

#         narrator "Despite knowing very little about it, and never taking a comp sci course in her life, she has decided\
#         to commit to her decision and go into the next chapter in her life."

#         narrator "Your job is to help Eza make choices and navigate through her 4 year journey at the University of Tokyo."

#         show screen game_stats

#         narrator "The choices you make will affect Eza's academics, mental and physical health, and relationships. Eza\
#         needs a certain amount of each category to function as a decent human being, and to proceed to the next year."

#         narrator "Depending on your choices you can also get additional points in a category or lose points. These types of
#         points are called sitautation points."

#         narrator "For instance, let's say you chose to made a nice breakfast, the choice itself has points associated with it. 
#         Now let's say you burned your hand making that breakfast, this was a concequence of the choice, NOT choice itself."

#         narrator "In this situation, you would loose points. However, if the concequence of making a nice breakfast lead to a good day, you would recieve
#         bonus points."

#         narrator "In essence, the effects of your choices you can lead to getting bonus points or losing points."

#         narrator "Make the right choices and Eza will graduate with a degree in computer science. Good luck!"
        
#         call loading 

#         jump night_before_orientation
    
#     ##############################################################################################
#     #night_before_orientation
#     ##############################################################################################
#     label night_before_orientation:

#         scene texting on phone with dissolve

#         narrator "{i}You're sitting in your room texting your friend Khushboo, who is also starting at the University of Tokyo.{/i}"

#         narrator "{i}You're trying to ignore it but the nerves are beginning to settle in. After taking a year off to work
#         all you're friends from high school are ahead and it feels like you're completely starting over.{/i}"

#         show khushboo talking at left
#         narrator "From Khushboo: Hey are u feeling about school?"
#         hide khushboo

#         show eza talking at right
#         narrator "From Eza: Worried I'm going to get lost but what's new lol"
#         hide eza

#         show khushboo talking at left
#         narrator "From Khushboo: I'll probably still get lost even though we walked to our classes the other day"
#         hide khushboo
        
#         show khushboo talking at left
#         narrator "From Khushboo: Are going to the orientation event tommorow?"
#         hide khushboo

#         show eza talking at right
#         narrator "From Eza: I was thinking about it..."
        
#         narrator "From Eza: Were you planning on going?"
#         hide eza

#         show khushboo talking at left     
#         narrator "From Khushboo: Yeah I think it's a good idea to go"
#         hide khushboo

#         menu: 
#             "Should Eza go to the event?"
#             "Yes" :
#                 $ relationship_points += 10

#                 show eza talking at right
#                 narrator "From Eza: Yeah I'd think it would be a good idea. I'll meet you there?"
#                 hide eza

#                 show khushboo talking at left
#                 narrator "From Khushboo: Yeah I'll see you there"
#                 hide khushboo

#                 call loading
#                 jump orientation_day_good_ending

#             "No" :
#                 $ relationship_points -= 10

#                 show eza talking at right
#                 narrator "From Eza: I don't think I'll be going"

#                 narrator "From Eza: have fun tho"
#                 hide eza 

#                 show khushboo talking at left
#                 narrator "From Khushboo: Thanks! I'll tell you how it goes"
#                 hide khushboo

#                 call loading
#                 jump orientation_day_bad_ending


    
#     ##############################################################################################
#     #orientation_day_good_ending
#     ##############################################################################################

#     label orientation_day_good_ending:

#         scene bus stop with dissolve 

#         narrator "{i}You've made it school without a hitch. The air is warm, you're sitting on a bench under listening to Lana del Rey as you wait for Khushboo.{/i}"

#         narrator "{i}Looking at you're phone, you see that there are 15 minutes to the event, it takes 10 minutes to walk across campus, and Khushboo isn't here yet.{/i}"

#         narrator "{i}You realize that she won't make it in time and shoot her a text.{/i}"

#         scene texting on phone with dissolve
        
#         show eza talking at left
#         narrator "From Eza: Hey do you want me to wait for you?"
#         hide eza

#         show khushboo talking at right
#         narrator "From Khushboo: No it's okay, I'm not going to make it in time. I'll see you later!"
#         hide khushboo

#         show eza talking at left
#         narrator "From Eza: Okay, see you later"
#         hide eza

#         scene courtyard with dissolve

#         narrator "{i}You're a bit anxious about going about this without you're friends, but you make the walk to the Engineering and Computer Science building\ 
#         and try to get situated.{/i}"

#         narrator "{i}The lady running registration asks for your name and hands you a name tag. She lets you know what group your in, you thank her and try to find\
#         these people.{/i}"

#         narrator "{i}You find the group and sit down. The groups grows to a considerable size, so you don't think that you'll be able to form any close relationship,
#         but you'll try.{/i}"

#         narrator "{i}You're all trying to figure out how to color in the team logo and they include you because you've briefly mentioned that you have done some art\
#         before. After finishing the logo you're team is dirrected to go do the activities.{/i}" 

#         scene lecture hall with dissolve

#         narrator "{i}You're brought into a large lecture hall, and spread around you are a bunch of robotics materials all spread out on the tables.{/i}"

#         narrator "{i}You try to participate, but you don't have any experience building or programming robots so you end up watching mostly.{/i}"

#         scene courtyard with dissolve

#         narrator "{i}The rest of the morning goes in the same manner. Eventaully you're team is brought back to the meeting area and pizza lunch is distributed 
#         to everyone. You text Khushboo to see where she is, but get no reply.{/i}"

#         menu:
#             "You see small groups of girls, do you go talk to one of them?"
#             "Yes" :
#                 $ relationship_points += 2
#                 $ will_to_survive_points -= 1

#                 narrator "{i}You walk over to a group and say hi. They're all in different programs and out of town, so it's harder to find something in common\
#                 to talk about. Since you live at home, you can't relate to being in res or the struggle of moving to a new city.{/i}"

#                 narrator "{i}Over the lunch break you go around talking to different groups, You're able to exchange information with some cool German exchange students.
#                 It's all small talk, nothing that your job in customer service couldn't have prepared you for.{/i}"

#             "No" :
#                 $ relationship_points += 0
#                 $ will_to_survive_points += 1 

#                 narrator "{i}You decide to find a nice spot in the shade and eat your pizza. There's been a lot of interactions all day and you've been around more people 
#                 in one day than you've had all summer. You know that you should probably socialize, so you tell yourself that you'll for sure do it tomorrow, in class.{/i}"

#         scene courtyard2 with dissolve

#         narrator "{i}After being unsucessful in finding you group after lunch, you end up running into Khushboo. Here you are introduced to a new friend, Angus, that Khushboo\
#         made while she was doing the activities with her team.{/i}"

#         show khushboo talking at left
#         khushboo "Hey Eza, how was your first day?"

#         hide khushboo talking
#         show eza talking at right
#         eza "Not too eventful, we built a lego version of the quad and built a robot. How about you guys?"

#         hide eza talking
#         show khushboo talking at left
#         khushboo "Our team kind of took over haha. We've just been hanging out while they've been doing the activities."
#         khushboo "This is Angus by the way."

#         hide khushboo talking
#         show angus talking at left
#         angus "Hey, nice to meet you."

#         hide angus talking
#         show eza talking at right
#         eza "Nice to meet you too. What program are you in?"

#         hide eza talking
#         show angus talking at left
#         angus "I'm in computer science."

#         hide angus talking
#         show eza talking at right
#         hide eza talking

#         narrator "{i}You're relieved to meet another person in computer science. You and Angus end up trading phone numbers and comparing schedules. 
#         You both notice that you are both in the same CSC 110 course. {/i}"

#         narrator "{i}Since Khushboo is in SEng you weren't going to be in the same classes, so
#         knowing someone else and being in the same class as them is relieving to hear.{/i}"

#         scene lecture hall with dissolve

#         narrator "{i}Since you lost you're group you assimilate into Angus and Khushboo's team. The groups are so big that no one really notices that
#         you joined. The team ends up in a lecture hall where the teams are tallying points won from the activites.{/i}"

#         narrator "{i}Each team leader stands and the president of the Engineering department, Jessica, calls out numbers like it's a bid \"10...20...30...40...
#         80...90...100...\"{/i}"

#         narrator "{i}Slowly team leads sit down until one is left \"...120 going once, going twice, we have a winner!\"{/i}"
        
#         show khushboo talking at left
#         khushboo "{i}That's our team lead standing up.{/i}"
#         hide khushboo talking

#         show angus talking at left
#         angus "{i}I guess it is{/i}"
#         hide angus talking

#         show khushboo talking at left
#         khushboo "{i}Since you've joined our team you win too!{/i}"
#         hide khushboo talking

#         scene sunset with dissolve
#         narrator "{i}The president takes you into one of the engineering building and hands out sweatshirts/hoodies.{/i}"
#         narrator "{i}The days activites are over and the three of you head off to the bus stop after a realtively enjoyable day at the University of Tokyo.{/i}"
        
#         call loading
#         jump first_day_good_ending

#     ##############################################################################################
#     #orientation_day_bad_ending
#     ##############################################################################################

#     label orientation_day_bad_ending:

#         scene bedroom with dissolve

#         narrator "{i}You're sitting in your room thinking about the event that you didn't go to. You decide not to think about it too deeply and\ 
#         try to enjoy the last day of summer. You make an iced coffee before going outside and cracking open a manga.{/i}"

#         narrator "{i}You spend the day reading and soaking up the last of the summer sun. In the evening you recieve a text from Khushboo.{/i}"
        
#         narrator "From Khushboo: Hey, how was your day?"

#         narrator "From Eza: It was good, I spent the day outside."

#         narrator "From Khushboo: That's nice, I went to the orientation event today. It was fun, I met a guy named Angus."
        
#         narrator "From Khushboo: He's in computer science too, I think you would like him."

#         narrator "From Eza: That's cool, I'm glad you had fun!"

#         narrator "From Khushboo: Yeah there were some activities and we won a prize. I'll tell you about it tomorrow."

#         narrator "From Eza: Can't wait to hear about it."
        
#         call loading
#         jump first_day_bad_ending

#     ##############################################################################################
#     #first_day_good_ending
#     ##############################################################################################

#     label first_day_good_ending:

#         scene outside lecture hall with dissolve

#         narrator "{i}Thankfully you did a walkthorugh with Khushboo the other day and walked to all your classes, so you're able to find your\
#         first class right away. Standing outside the door you catch a familiar glimps of blonde hair.{/i}"

#         show eza talking at right
#         eza "Hey Angus, how you doing?"
#         hide eza

#         show angus talking at left
#         angus "Pretty good, what about you?"
#         hide angus

#         show eza talking at right
#         eza "I'm doing alright."
#         hide eza

#         scene lecture hall with dissolve

#         narrator "{i}The two of you head in the lecture hall and find a seat in the middle. After coming back from the pandemic it's a\
#         bit overwhelming seeing over 200 students in one space.{/i}"

#         narrator "{i}The professor, Dr. Dr. Berg Berg,comes in and starts talking about the course and the syllabus. There's a lot of things to do in this class\
#         weekly assignments and labs, pre-lecture videos and quizzes, and of course midterms and a final.{/i}"

#         narrator "{i}Dr. Berg finishes the housekeeping and starts going over some programming concepts, and encourages everyone to program along.{/i}"

#         narrator "{i}You pull out your laptop and enter the password, after a moment you read that the password is incorrect. You try again and again, but it's not working.{/i}"

#         narrator "{i}You feel like a joke, why can't you remember what your password is. No to mention, this is your first time owning a laptop.{/i}"
        
#         narrator "{i}Even though they're proabably not, you hope that the people behind you don't see you struggle. As you try to figure out your password,\
#         Dr. Berg is moving on with her demo and can't help but feel like you're behind.{/i}"  

#         menu:
#             "What do you do? Do you keep trying or do you ask Angus if you can follow along with what he's doing?"
            
#             "Ask Angus":

#                 $ relationship_points += 5
#                 $ academic_points += 5
#                 $ will_to_survive_points -= 5

#                 narrator "{i}You lean over to Angus and ask if you can follow along with what he's doing.{/i}"

#                 show eza talking at right
#                 eza "Hey, would you mind if I follow along with what you're doing?"
#                 hide eza

#                 show angus talking at left
#                 angus "Yeah, for sure."
#                 hide angus talking

#                 narrator "{i}As you watch Angus and her program, questions keep coming to your head.{/i}"

#                 narrator "{i}She's talking about a function, what is a function? What is this \"foo\" that she's talking about?{/i}"

#                 narrator "{i}Nothing really makes sense, and your confused with what's going on.{/i}"

#                 narrator "{i}This is supposed to be an introduction to computer science, why doesn't it feel that way.{/i}"

#             "Keep trying to figure out the password":

#                 $ relationship_points += 0
#                 $ academic_points -= 5
#                 $ will_to_survive_points -= 10

#                 narrator "{i}You keep trying to figure out the password, but you're not able to get it.{/i}"

#                 narrator "{i}You feel pathetic and overwhelmed for not being able to figure out something so simple.\
#                 You end up being so wrapped up in this that you are unable to hear what Dr. Berg is saying.{/i}"

#                 narrator "{i}You keep trying until you MacBook disables itself. During this period, behind you there are two boy. Even though they're trying to whisper
#                 you can hear them saying, \"What's a girl like her doing in this class?\"{/i}"

#                 narrator "{i}You know you're not the only one who heard their comments, because Angus turns and gives you a sympathetic look.{/i}"

#                 narrator "{i}Your ears brun red and tears sting behind your eyes.{/i}"

#                 narrator "{i}What are you even doing here. You can't even get your MacBook to work. How are you supposed to learn computer science.{/i}"
                
#                 call loading
        
#         scene lecture hall with dissolve

#         narrator "{i}You end up trying our password one more time before class finishes. With an exasperated sigh, you see that it works\
#         even though you swear you've tried that one before.{/i}"
        
#         narrator "{i}When class ends, you and Angus pack up and head out of the lecture hall to meet with Khushboo.{/i}"

#         call loading
#         jump school_schedule


#     ##############################################################################################
#     #first_day_bad_ending
#     ##############################################################################################

#     label first_day_bad_ending:

#         scene lecture hall with dissolve

#         narrator "{i}Thankfully you did a walk thorugh with Khushboo the other day, so you're able to find your first class right away.\
#         Entering the class you feel a bit overwhelemed.{/i}"

#         narrator "{i}There isn't anyone there that looks familiar, and coming back from the pandemic it's a bit overwhelming being around over 200.\
#         Quickly, you look for an empty seat and sit down and the professor begins the first lecture.{/i}"

#         narrator "{i}The professor, Dr. Dr. Berg Berg, comes in and starts talking about the course and the syllabus. There's a lot of things to do in this class\
#         weekly assignments and labs, pre-lecture videos and quizzes, and of course midterms and a final.{/i}"

#         narrator "{i}Dr. Berg finishes the housekeeping and starts going over some programming concepts, and encourages everyone to program along.\
#         You pull out your laptop and enter the password, after a moment you read that the password is incorrect. You try again and again, but it's not working.{/i}"

#         narrator "{i}You feel like a joke, why can't you remember what your password is. No to mention, this is your first time owning a laptop.{/i}"
        
#         narrator "{i}Even though they're proabably not, you hope that the people behind you don't see you struggle. As you try to figure out your password,\
#         Dr. Berg is moving on with her demo and can't help but feel like you're behind.{/i}"  

#         menu:
#             "What do you do? Do you sit there and try to focus on the lecture without doing the exercise, or try to fix the laptop?"
            
#             "Sit there and try to focus on the lecture":

#                 $ relationship_points += 5
#                 $ academic_points -= 5
#                 $ will_to_survive_points -= 5

#                 narrator "{i}You close the laptop and try you're best to focus on what Dr. Berg is saying.{/i}"

#                 narrator "{i}As you watch her program and explain, questions keep coming to your head.{/i}"

#                 narrator "{i}She's talking about a function, what is a function? What is this \"foo\" that she's talking about?{/i}"

#                 narrator "{i}Nothing really makes sense, and your confused with what's going on.{/i}"

#                 narrator "{i}This is supposed to be an introduction to computer science, why doesn't it feel that way.{/i}"

#             "Try to fix the laptop":

#                 $ relationship_points += 0
#                 $ academic_points -= 5
#                 $ will_to_survive_points -= 10

#                 narrator "{i}You keep trying to figure out the password, but you're not able to get it.{/i}"

#                 narrator "{i}You feel pathetic and overwhelmed for not being able to figure out something so simple. \
#                 You end up being so wrapped up in this that you are unable to hear what Dr. Berg is saying.{/i}"

#         narrator "{i}You end up trying our password one more time before class finishes. With an exasperated sigh, you see that it works\
#         even though you swear you've tried that one before.{/i}"
        
#         narrator "{i}When class ends, you pack up and head out of the lecture hall to meet with Khushboo.{/i}"

#         call loading 

#         scene courtyard2 with dissolve

#         narrator "{i}As you walk up to Khushboo you notice a blonde haired boy beside her.{/i}"

#         show khushboo talking at left
#         khushboo "Hey Eza, this is Angus. He's in computer science too."
#         hide khushboo 

#         show angus talking at left #BUG HERE
#         angus "Hey, nice to meet you."
#         hide angus

#         show eza talking at right
#         eza "Nice to meet you too!"
#         hide eza 

#         narrator "{i}The three of you have lunch and go on about orientation day and the first day of class. Apparently Khushboo met Angus during\
#         orientation and became good friends over the course of the day. Angus seems really nice, it's easy to joke around with him.{/i}"

#         narrator "{i}The two of you so happen to be in the same CSC 110 class. You and Angus both agree that next time you have class, the two of\
#         you should meet up and sit next to each other.{/i}"

#         call loading
#         jump school_schedule

#     ##############################################################################################
#     #school_schedule
#     ##############################################################################################

#     label school_schedule:

#         scene bedroom with dissolve 

#         narrator "{i}You start getting into the swing of things, and you're able to find your classes and get into the routine of things.\
#         You're taking Math 122, CSC 110, FRAN 170, and ENGL 142, a good mix of things.{/i}"

#         narrator "{i}As the weeks go by everything begins to feel monotonous. Wake up at 6:30, get dressed, take the bus, go to youe 8:30AM class\
#         go hang out with Angus until Math 122, have lunch alone, go to French, and then go home, do homework, go to bed, repeat.{/i}"

#         narrator "{i}You're not really sure what you're doing, but you're doing it. You're not really sure if you're happy, but you're not really\
#         sad either. You're just kind of there, and you're not really sure if you're okay with that.{/i}"

#         narrator "{i}French and English are going well, but you're struggling with Math and Computer Science. You're not really sure what's going on.\
#         At least with the computer science you can make it mostly with trial and error, but with math it feels like it's not even math anymore.{/i}"

#         narrator "{i}When your prof started going on about logical implications and two falses implying a true, you lost it. Everything seemed broken\
#         and didn't make sense anymore.{/i}"

#         narrator "{i}Everyone except for you seems to know what they're doing...{/i}"

#         call loading
        
#         scene math class with dissolve

#         narrator "{i}You're sitting at the end of math 122 with your laptop open. The grades for the last assignment have just come out.\
#         You have barely managed to scrape through with a 50%%.{/i}"

#         $ academic_points -= 10
#         $ will_to_survive_points -= 10

#         narrator "{i}This makes you freeze, you've never for less than 90%% in your assignments before, and this was the first assignment for this class.\
#         It can only get harder from here.{/i}"

#         menu:
#             "Do you decide to reach out to your professor for help or not?"
#             "Yes, get help":
#                 narrator "{i}You feel absolutely gutted. You're stomach has a stone in it, your heart is your throat, and you're doing everything in you're\
#                 power to keep the tears at bay.{/i}"

#                 narrator "{i}You take some breaths and focus on packing up. You leave the classroom and find a quite space to have a Zoom meeting. You wait\
#                 contemplating the choices that got you to this place.{/i}"

#                 call loading

#                 scene myanhardt office with dissolve

#                 narrator "{i}The time comes and you jump on the zoom link, camera off you wait until everyone else is done talking before you request to talk\
#                 to her in a breakout room.{/i}"

#                 narrator "{i}The two of you go over your assignment, and you know what you got wrong were just things you didn't know. But then she asks you\
#                 something unexpected.{/i}"

#                 drMyanhardt "{i}Do you have friends in this class?{/i}"

#                 narrator "{i}You're taken aback by the question.{/i}"

#                 eza "Yes, I have a friend in this class."

#                 narrator "{i}Even though that's clearly a lie{/i}"

#                 drMyanhardt "{i}I think it would be a good idea to form a study group with them. I think that would be beneficial for you..."

#                 narrator "{i}The conversation ends and it didn't really help as much as you thought it would.{/i}"

#                 narrator "{i}However, in hindsight, the world didn't end when you asked for help.{/i}"

#                 $ academic_points += 0
#                 $ will_to_survive_points += 5
#                 $ relationship_points += 5

#                 narrator "{i}After office hours you decide that enough is enough, and that if you need assistance, you need assitance.\
#                 There's nothing wrong or shameful in needing help.{/i}"

#                 scene masc with dissolve

#                 narrator "{i}As soon as you find the time, you go to the math and stats assistance center to ask for help. With renewed determinations\
#                 and questions in mind you put yourself down on a list and wait.{/i}"

#                 narrator "{i}Soon you meet with a tutor, but realize that their teaching style in not meant for you. While you have a better understanding\
#                 of what you need to do, you need more help and time to master the concepts.{/i}"

#                 menu:
#                     "Do you find an outside tutor?"
#                     "Yes":
#                         call loading
#                         jump find_a_tutor_good_ending
#                     "No":
#                         call loading
#                         jump find_a_tutor_bad_ending
            
#             "No, don't get help":

#                 scene bus stop with dissolve

#                 narrator "{i}You pack up as fast as you can. The blood is rushing to your ears and all you can think about is getting home as fast as possible.\
#                 The weight in your stomach grows and all you can do is hope to keep your emotions in check until you get home.{/i}"

#                 $ academic_points -= 10
#                 $ will_to_survive_points -= 5
#                 $ relationship_points -= 0

#                 scene bedroom with dissolve 

#                 narrator "{i}You get home and you're able to keep it together until you get to your room. You close the door and let the tears fall.{/i}"
#                 narrator "{i}Once you pickc yourself up you decide to take a look at the next assignment, it really doesn't look any better than the first. But\
#                 you sit yourself down and try to crack at it {/i}"

#                 call loading

#                 scene desk with dissolve
            
#                 narrator "{i}After hours of screening through your notes, the textbook, and examples, but nothing there's nothing but the question number on\
#                 your paper. With a deep sigh you close your books and head to bed.{/i}"

#                 narrator "{i}This trend continues, days pass, and you're getting closer and closer to the deadline.{/i}"

#                 narrator "{i}After another unsucessful study session, in bed, you think to yourself \"I can\'t let this go one any further\".{/i}"

#                 call loading

#                 scene masc with dissolve

#                 narrator "{i}The next day you go to the math and stats assistance center to ask for help. With renewed determinations and questions in mind you put\
#                 yourself down on a list and wait.{/i}"

#                 narrator "{i}Soon you meet with a tutor, but realize that their teaching style in not meant for you. While you have a better understanding of what\
#                 they're saying. You need more help and time to master the concepts.{/i}"

#                 narrator "{i}You decide to try again with another tutor, but the same thing happens. This cycle continues until the math and stats center closes.{/i}"

#                 narrator "{i}You go home and turn in what you have, complpetely unsatisfied with the work you've turned in, and the time you've spent on this class.{/i}"

#                 call loading 
#                 jump mental_health_talk

#     ##############################################################################################
#     #find_a_tutor_good_ending
#     ##############################################################################################

#     label find_a_tutor_good_ending:

#         scene math tutoring with dissolve
        
#         narrator "{i}After being unsucessful at the math and stats help center you go looking for external help. You go online and look for a math tutor in your area.
#         You come across one man, Ryan, and reach out to him for help{/i}."

#         narrator "{i}You meet with him and he's able to help you understand the concepts that you're struggling with.{/i}"
#         narrator "{i}You're able to get the help that you need\
#         you leave the tutoring session feeling better about what you're doing at school and some of that pressure has been lifted.{/i}"

#         call loading 
#         jump find_friends_in_math122

#     ##############################################################################################
#     #find_a_tutor_bad_ending
#     ##############################################################################################

#     label find_a_tutor_bad_ending:

#         scene masc with dissolve

#         narrator "{i}You decide against finding a tutor, they're expensive and you don't know if there are people capable of helping you with this kind of material.\
#         As a result you continue to go to the math and stats assistance center.{/i}"

#         narrator "{i}You go several times a week, and it's the same outcome each time. You leave half understanding what you came into understand.{/i}"
#         narrator "{i}It feels disheartening, you're trying your best, so are the tutors, but nothing seems to click 100%%{/i}"

#         call loading
#         jump find_friends_in_math122

#     ##############################################################################################
#     #find_friends_in_math122
#     ##############################################################################################

#     label find_friends_in_math122:

#         scene math class with dissolve

#         narrator "{i}Stepping into you're 122 you recall the first time you had this class. You came early and there weren't that many people there at first.\
#         However, as the start time approached you noticed seats fill with more men than women.{/i}"
        
#         narrator "{i}Of the few women that entered the class, there was one who didn't seem to already be in a friend group.{/i}"

#         narrator "{i}You see that girl again sitting next to some boy.{/i}"

#         menu:
#             "Do you go sit next to her"
#             "Yes":
#                 $ relationship_points += 5
#                 $ will_to_survive_points += 5

#                 narrator "{i}You walk over to her and sit down. You introduce yourself and she introduces herself as well.{/i}"

#                 show eza talking at right
#                 eza "Hey, I'm Eza."

#                 hide eza 
#                 show imen talking at left
#                 imen "Hi, 'm Imen."

#                 hide imen
#                 narrator "{i}The two of you exchange small talk until Dr. Myanhardt begins her lessons. At the end of class the two of you exchange your\
#                 goodbyes and you hope that you can kindle this relationship.{/i}"
#                 $ met_imen = True

#                 call loading
#                 jump mental_health_talk

#             "No":
#                 $ relationship_points -= 5
#                 $ will_to_survive_points -= 5
    
#                 narrator "{i}As more people filter in and sit down around her, it seems like she already has an established friend group. Feeling shy, you decide to sit in the same\
#                 spot as you always do.{/i}"

#                 narrator "{i}Immediatly after sitting down you, regret not going up there. Because even if you didn't talk, at least you tried.{/i}"

#                 call loading
#                 jump mental_health_talk

#     ##############################################################################################
#     #mental_health_talk
#     ##############################################################################################

#     label mental_health_talk:

#         scene kitchen with dissolve 

#         narrator "{i}Since university has started your mental health has slowly declined. The constant stress of deadlines has your motivation flagging.\
#         You've been in a haze for what feels like ages. Going through the motions of life. {/i}"

#         narrator "{i}Your in the kitchen making spicy fire noodles when your mom walks in. She asks how you're doing and you don't know how to respond.{/i}"

#         menu:
#             "Tell her you're doing fine or lie"
#             "Tell her you're doing fine":

#                 $ will_to_survive_points -= 5
#                 $ relationship_points += 5

#                 narrator "{i}You tell her that you're not doing fine.{/i}"

#                 narrator "{i}You want to tell her you feel drained and feel as though you're not really \"here\"{i}."

#                 narrator "{i}She tells you not to stress that much and that you only need to pass, and that you don't have to hold yourself to such a high standard.\
#                 You know that. But she raised you this way, to always expect nothing but the best from yourself. The contradiction in what you've grown up with\
#                 and her attitude now don't help with what you're feeling.{/i}"

#                 call loading
#                 jump friendship_with_angus_and_khushboo

#             "Lie":
#                 $ will_to_survive_points -= 5
#                 $ relationship_points -= 5

#                 narrator "{i}You tell her that you're doing fine. She looks at you for a second, but she's doesn't to press the issue.
#                 She leaves you to your noodles, and you're glad that you don't have interact with anyone.{/i}"

#                 narrator "{i}You want to tell her you've been feeling, but you're not really sure yourself.\
#                 Nothing horrific has happened, you've just felt drained and feel as though you're not really \"here\"{i}."

#                 narrator "{i}You wish you could talk to her about these things, but these conversations have never gone down well in the past.\
#                 She'd go on about her life and how difficult it was immigrating to a new country and starting over at a new university.{i}"
               
#                 narrator "{i}You know how difficult it was for her, so your problems seem insignificant in comparison.{/i}"

#                 call loading
#                 jump friendship_with_angus_and_khushboo

#     ##############################################################################################
#     #friendship_with_angus_and_khushboo
#     ##############################################################################################
#     label friendship_with_angus_and_khushboo:

#         scene courtyard with dissolve 

#         narrator "{i}There are some people who do understand you're struggle though. Maybe not to the same extent, but they are living in the trenches with you.{/i}"

#         narrator "{i}You've known Khushboo since the end of high school and went to hair school together. This is where you both banded together with another boy\
#         named Ethan, to survive being with \"blondes\" for 9 months.{/i}"

#         narrator "{i}She's someone that you trust, respect, and love dearly. Even though she's in a different program, and you don't see her as much as before,\
#         you're glad you're doing this together. You're two women trying to help each other succeed through this degree.{/i}"

#         narrator "{i}On the other hand, you've known Angus only for a few weeks, but you see and talk to each other nearly every day. It's easy being friends with Angus.\
#         He's open and nonjudgemental, which has made it easy for you to ask him for help in CSC 110.{/i}"
        
#         narrator "{i}He's kind and never pokes fun at you for not understanding what's\
#         happening in the code.{/i}"
        
#         narrator "{i}The two of you often study together, he helps you with computer science, and you contructively rip his papers to shreads in English. (You'd like to\
#         think that you're pretty good, despite the allegations of computer scientist being unable to write.){/i}"
        
#         narrator "{i}He's very much a girl's girl, and a ally to both you and Khushboo.{/i}"

#         call loading
#         jump work_life_balance
            
#     ###############################################################################################
#     #work_life_balance
#     ###############################################################################################

#     label work_life_balance:
        
#         scene bedroom with dissolve 

#         narrator "{i}At school you're starting to find your footing, balancing classes, assignments, tutoring, friendships, and other commitments.\
#         There is one thing that has been on your mind, the CSC 110 labs.{/i}" 
        
#         narrator "{i}You've been mostly doing them on the weekends because your weeks are so busy.\
#         However, that has cut into your time to rest.{/i}"

#         menu:
#             "Do you continue to do the labs on the weekends or do you try to find time during the week?"
#             "Continue to do the labs on the weekends":
#                 $ will_to_survive_points -= 5
#                 $ academic_points += 5

#                 narrator "{i}You continue to do the labs on the weekends, but you're not able to get as much rest as you need.\
#                 It takes a few hours out of your time and adds to the list of things to do over the weekend: laundry, meal prep,\
#                 washing the dishes...{/i}"

#                 narrator "{i}The lab have always been a point of stress for you though. They are not worth an insiginificant amount of marks\
#                 and they help prepare you for the assignments.{/i}"
                
#                 narrator "{i}So despite the extra chunk of time taken awayfrom the weekend, you now go into\
#                 labs with more peace of mind. By doing this you've also got into a routine for all your classes.{/i}"

#                 call loading
#                 jump classes_get_harder 

#             "Try to find time during the week":
#                 $ will_to_survive_points -= 5
#                 $ academic_points -= 5

#                 narrator "{i}You decide to try to find time during the week to do the labs. You're able to find time during the week to do the labs.\
#                 You're feeling more and more drained as the weeks go by.{/i}"

#                 call loading
#                 jump classes_get_harder

#     ###############################################################################################
#     #classes_get_harder
#     ###############################################################################################
#     # narrator "{i}{/i}"

#     label classes_get_harder:

#         scene desk with dissolve 

#         narrator "{i}With midterms turning their ugly head, life is not getting any easier for anybody. It seems that you professor are trying to make you fail.\
#         \"You have two midterms on the same day, too bad\". There's no accomodation in STEM.{/i}"

#         narrator "{i} Having assignments, labs, and lectures on top of trying to study for upcoming midterms all at once has been overwhelming.\
#         You're constantly onto the next thing. Even when you do give yourself a 5 minute break, you feel guilty about taking that time.{/i}"

#         call loading

#         scene math class with dissolve 

#         narrator "{i}Like most Wednesday mornings you find yourself in math class{/i}"

#         if (met_imen):
#             narrator "{i}You spot Imen sitting with a group of guys.{/i}"

#             menu:
#                 "Do you go sit with Imen and those guys at the front or do you find a seat in the middle?"

#                 "You find a seat in the middle":

#                     narrator "{i}You find a seat in the middle and get set up for class. While you're waiting for the professor to start the lecture you take\
#                     a look over your assignment.{/i}"

#                     narrator "{i}You would have loved to be able to confirm you're results with someone else taking this class. But at this point, you feel like everyone\
#                     has found their group. It would be weird for you to join one now.{/i}"

#                     if (has_tutor):

#                         $ academic_points += 5
#                         $ will_to_survive_points -= 5
#                         $ relationship_points -= 5

#                         narrator "{i}While it would be nice for you to have friends in this class, in the end, all you need to do is pass with a decent mark. i.e nothing less\
#                         than 80%%. You've got a scholarship to keep up!{/i}"

#                         narrator "{i}Besides you're sessions with Ryan have been paying off. The marks have been increasing on each assignment.{/i}"
                    
#                     else:

#                         $ academic_points -= 5
#                         $ will_to_survive_points -= 5
#                         $ relationship_points -= 5

#                         narrator "{i}All the assignments have been going the same way so far...50%%-60%%. It's obvious that you're barely holding on. You can kiss that renewable
#                         scholarship goodbye. You think that in terms of passing the class, you could probably scape by. But that's something you don't even want to consider right now.{/i}"

#                     call loading
#                     jump office_hours_csc110
                    
#                 "You sit with Imen and those guys":

#                     $ academic_points += 10
#                     $ will_to_survive_points += 10
#                     $ relationship_points += 10

#                     narrator "{i}You take a breath and make your way over to the group, everyone look at you for a second before Imen speaks up.{/i}"

#                     show imen talking at left
#                     imen "Hi Eza, how's it going?"
#                     hide imen

#                     show eza talking at right
#                     eza "I'm doing as good as I can be. How about you?"
#                     hide eza

#                     show imen talking at left
#                     iman "Not to bad this home work is killer though."
#                     hide iman

#                     show eza talkinga at right
#                     eza "Tell me about it. I'm almost done, but it's been brutal."
#                     hide eza

#                     show imen talking at left
#                     imen "Me and the guys are almost done too. We're going to work on it today, do you want to join us?"
#                     hide imen

#                     show eza talking at right
#                     eza "For sure!"
#                     hide eza

#                     narrator "{i}After class you and Imen exchange numbers and agree to meet at the library later tonight.{/i}"

#                     call loading

#                     narrator "{i}Later that night you meet Imen and her friends at the library and have a very productive evening.{/i}"

#                     narrator "{i}You guys meld really well together and are able finish the questions early on in the evening. Without even noticing it,
#                     you guys spend a good couple hours just talking.{/i}"     

#                     narrator "{i}Leaving the library, even though you wasted a bunch of time talking, you feel satisfied with yourself.{/i}"

#                     call loading
#                     jump office_hours_csc110      

#         else:
#             if (has_tutor):

#                 $ academic_points += 5
#                 $ will_to_survive_points += 0
#                 $ relationship_points += 0

#                 narrator "{i}While it would be nice for you to have friends in this class, in the end, all you need to do is pass with a decent mark. i.e nothing less\
#                 than 80%%. You've got a scholarship to keep up!{/i}"

#                 narrator "{i}Besides you're sessions with Ryan have been paying off. The marks have been increasing on each assignment.{/i}"

#                 narrator "{i}Since you went to office hours, you've been asking Dr. Myanhardt questions after class whenever you're unsure of something.{/i}"

#             else:

#                 $ academic_points -= 5
#                 $ will_to_survive_points -= 5
#                 $ relationship_points += 0
                
#                 narrator "{i}All the assignments have been going the same way so far... 50%% - 60%%. It's obvious that you're barely holding on. You can kiss that renewable\
#                 scholarship goodbye. You think that in terms of passing the class, you could probably scape by.{/i}"

#                 narrator "{i}But that's something you don't even want to consider right now.{/i}"

#             narrator "{i}There's the midterm that's coming up, that's been pushed to the back burner in the back of your mind. For now you're trying to focus on
#             making it one day at a time.{/i}"

#             call loading
#             jump office_hours_csc110

#     ###############################################################################################
#     #office_hours_csc110
#     ###############################################################################################
#     # narrator "{i}{/i}"

#     label office_hours_csc110:

#         scene desk with dissolve 

#         narrator "{i}Not only is the Math 122 midterm rearing it's head, but so is the CSC 110 midterm. You panicked at first when you heard that it 
#         was going to be on paper; since you've gotten through the assignments and labs by trial and error.{/i}"

#         narrator "{i}But after taking a breath and you just commited to kicking it to high gear and locking in on your studies.{/i}"

#         narrator "{i}In an effort to get as much practice and master the material you decide to go over labs, lectures, quizzes, and assignments.{/i}"

#         menu:
#             "Do you go to office hours for help or do you try to figure it out on your own?"

#             "Figure it out on your own":

#                 $ academic_points += 5
#                 $ will_to_survive_points += 5
#                 $ relationship_points += 0

#                 narrator "{i}As soon as class ends, you hop on the bus back home. Once you've made it back of grab a snack and head straight to your bedroom. You lock\
#                 your door, throw your phone onto the bed, pull out your laptop and pull up this weeks assignment.{/i}"

#                 narrator "{i}With another tab open to cover the cody body, you go through each method one by one writing what you think the logic would be on a piece of paper.
#                 Once you've finished the question, you unconver it and make corrections.{/i}"

#                 narrator "{i}After doing this exercise a couple more times, you begin to get the hang of coding on paper. Moving on, you go back to the previous quizzes.
#                 These are harder to answer, not because they're difficult but because you can remember what you put down previously.{/i}"

#                 show eza talking at right

#                 eza "Maybe I can do this...it's not as bad as I thought it was going to be."
#                 hide eza 

#                 eza "With the momentum, you continue to study late into the night."
#                 call loading
#                 jump write_math122_midterm

#             "Go to office hours":

#                 $ academic_points += 5
#                 $ will_to_survive_points += 5
#                 $ relationship_points += 5
                
#                 scene lecture hall with dissolve 

#                 narrator "{i}After class is over you meet with Khushboo and head over to one of the big lecture halls. The Women in Engineering and Computer Science club\
#                 (WECS) are hosting a review session for CSC 110.{/i}"

#                 narrator "{i}Maybe because it's so late in the evening, but it's only you Khushboo, two TAs, and Dr. Berg are in the room. It's almost silent, as 
#                 quietly as possible the two of you sit in the aisle.{/i}"

#                 narrator "{i}Khushboo works on her homework while you're trying to go through this weeks assignment. You're so stumped on this problem that you haven't notice
#                 that Dr. Berg has walked up to you and is looking over your shoulder.{/i}"

#                 show celina talking at left 
#                 celina "Hey, how's it going?"
#                 hide celina

#                 show eza surprised at right 
#                 eza "It's going okay, I'm just stuck on this question."
#                 hide eza 

#                 show celina talking at left
#                 celina "What are you stuck on?"
#                 hide celina

#                 narrator "{i}You show her the question.{/i}"

#                 show celina talking at left
#                 celina "{i}Where do you think you should start?{/i}"
#                 hide celina 

#                 narrator "{i}Honestly you don't even know where to start. That's why you've been looking at it for ten mintues.{/i}"

#                 menu:
#                     "Tell Dr. Berg that you don't know where to start or do you come up with something that's probably wrong?"

#                     "Tell Dr. Berg that you don't know where to start":

#                         $ academic_points -= 5
#                         $ will_to_survive_points -= 5
#                         $ relationship_points += 5

#                         narrator "{i}You were not expecting her to come up to you and ask you if you needed help so directly. With the room being almost silent it feels
#                         like you've just been called out. The thoughts that you're having are completely irrational.{/i}"

#                         narrator "{i}However, it feels like by admitting to not knowing, you're admitting that don't belong with the rest of the intellecutals here.{/i}"

#                         narrator "{i}In an anxious rush you blurt out{/i}"

#                         show eza anxious at right
#                         eza "I don't know where to start."
#                         hide eza

#                         narrator "{i}Dr. Berg nods and takes a look at the questions.{/i}"

#                         narrator "{i} She starts to explain what we need to accomplish in this question, but you can't follow. You're mind is spiraling.{/i}"

#                         show celina talking at left
#                         celina "{i}We need to create a list of all the student SIDs, how can we go about doing that?{/i}"
#                         hide celina

#                         narrator "{i}She looks at you expectantly. You probably know this, but your anxiety has taken off and your head is empty. All you can think about is messing
#                         up infront of her.{/i}"

#                         narrator "{i}Time is ticking. All you can do is stare at the screen.{/i}"

#                         narrator "{i}You must have taken too long because Dr. Berg chimes in.{/i}"

#                         show celina talking at left
#                         celina "{i}How can you go through a list of students?{/i}"
#                         hide celina 

#                         narrator "{i}You blurt something out...It must have been so wrong because she looks at you blanky before proceeding to explain the logic.{/i}"

#                         narrator "{i}You can't even listen to what she's saying because it feels like everything that you thought about was true.{/i}"
                        
#                         narrator "{i}Thinking about the guys in you're class who've been doing this since high school, you have no idea how you're going to catch up. You don't belong with these people.{/i}"
                    
#                     "Come up with something that's probably wrong":

#                         $ academic_points -= 5
#                         $ will_to_survive_points -= 5
#                         $ relationship_points += 5

#                         narrator "{i}You don't know what posseses you, in your mind you know it's not right, but your words come out with full confidence and strength.{/i}"

#                         show eza talking at right
#                         eza "An if statement"
#                         hide eza 
                        
#                         narrator "{i}For a second she gives you a blank look.{/i}"

#                         show celina confused at left
#                         celina "Good try..."
#                         hide celina 

#                         narrator "{i}She then proceeds to explain the logic behind the question.{/i}"

#                         narrator "{i}You can't even listen to what she's saying because you feel like an idiotic fraud. Thinking about the guys in you're class who've 
#                         been doing this since high school, you have no idea how you're going to catch up. You don't belong with these people.{/i}"

#                 narrator "{i}After she finishes explaining the question you thank her and lean over Khushboo and whisper.{/i}"

#                 show eza indifferent at right
#                 eza "I've finished asking all my questions, lets go?"
#                 hide eza 

#                 show khushboo talking at left
#                 khushboo "Sure, let's go."
#                 hide khushboo

#                 narrator "{i}You and Khushboo leave the room and head to the bus stop.{/i}"

#                 narrator "{i}What happened during office hours was mortifying. Aside from the embarassment, this experience has you really doubting yourself.
#                 Not just for the midterm, but for the future.{/i}"
                
#                 narrator "{i}If you're just scarping my computer science classes now, with the support of your friends and 
#                 people like the WECS, how are you going to stand in a field dominated by men.{/i}"

#                 $ went_to_office_hours = True

#                 call loading
#                 jump write_math122_midterm

#     ##############################################################################################
#     #write_math122_midterm
#     ##############################################################################################

#     label write_math122_midterm:

#         scene math class with dissolve

#         narrator "{i}Soon enough the Math 122 rolls around, hardly anytime after the CSC 110 midterm.{/i}"

#         narrator "{i}The classroom is packed like sardines. On regular days 60%% of the class doesn't show up, so to see everyone here is a lot.
#         Like the last midterm everyone is radiating nervious energy.{/i}"

#         narrator "{i}You take a seat at one of the chairs. This classroom sucks for midterms in particular, not just because it is small but, beacause
#         the chairs are arm desks. So there's hardly any space for your paper, let alone any stationary.{/i}"

#         narrator "{i}A TA distributes the tests face down. As they come around you sit cramped between two other students with your pencils and eraser in
#         your lap.{/i}"

#         narrator "{i}Once all the papers have been distrbuted Dr. Myanhardt says some words.{/i}"

#         show drMyanhardt talking at left
#         drMyanhardt "{i}You have 50 minutes for the midterm, the TAs will write the time on the board every 10 minutes. If you get stuck on a question 
#         move onto the next, ration you're time wisely. {/i}"
#         hide drMyanhardt

#         narrator "{i}Dr Myanhardt looks at the time and announces,{/i}"

#         show drMyanhardt talking at left
#         drMyanhardt "You may begin."
#         hide drMyanhardt

#         narrator "{i}As soon as she says that, there is a great rustle of paper.{/i}"

#         narrator "{i}You take a deep breath and open your test. You flip through each of the pages.{/i}"

#         if met_imen and has_tutor:
#             narrator "{i}Skimming through the pages, everything looks familiar. You've done similar questions before in your practice.{/i}"

#             narrator "{i}Studying late nights with Imen and meeting with Ryan have really helped you get familiar with the topics.{/i}"
        
#         elif met_imen and not has_tutor:
#             narrator "{i}Skimming through the pages, everything look familiar. You've done most of these quesions correctly in your practice.{/i}"

#             narrator "{i}Meeting Imen and forming a study griup with her have really helped you get familiar with the topics.{/i}"
             
#         elif not met_imen and has_tutor:
#             narrator "{i}Skimming through the pages, everything looks familiar. You've done most of these quesions correctly in your practice.{/i}"

#             narrator "{i}Doing the weekly sessions with Ryan have really helped you get familiar with the topics.{/i}"

#         else:
#             narrator "{i}Skimming through the pages, you've seen everything before. But you're at a loss at how to answer the questions.{/i}"

#         narrator "{i}You take breath, put your head down, and begin answering questions.{/i}"

#         call loading

#         scene math class with dissolve

#         narrator "{i}Time is ticking and your furisously trying to write and come up with something for this final long answer proof question.{/i}"

#         narrator "{i}Viciously your scribiling down words, the text getting larger and messier.{/i}"

#         narrator "{i}You're stuck. How do you prove the opposite direction of this if and only if proof?{/i}"

#         show drMyanhardt talking at left
#         drMyanhardt "5 minutes left."
#         hide drMyanhardt

#         narrator "{i}You're stressed, you're haven't finished this question, and have yet to look over your test.{/i}"

#         narrator "{i}Screw it you think. You drop this last question and go back to the first.{/i}"

#         narrator "{i}With the last 5 minutes you quickly glance over the rest of your test for glaring mistakes.{/i}"

#         show drMyanhardt talking at left
#         drMyanhardt "Time's up. Stop writing or else it's a 0!"
#         hide drMyanhardt

#         narrator "{i}You put your pencil down and sit back in your chair. You're exhausted.{/i}"

#         narrator "{i}A TA comes to collect you test while. Slowly you pick up your things and begin to pack up. You can hear others talking about the test
#         but you ingore it. If anything, if you hear them say something contradictory to what you did, it's only going to make you feel worse.{/i}"


#     if met_imen:
#         narrator "{i}Stepping out of the class you see Imen waiting for you.{/i}"

#         show imen talking at left
#         imen "How did you find the test?"
#         hide imen

#         show eza talking at right
#         eza "It was okay, I think I did enough to pass. What about you?"
#         hide eza

#         show imen talking at left
#         imen "I think I did okay too. Do you have anymore midterms?"
#         hide imen

#         show eza talking at right
#         eza "Yeah, I have one for CSC 110."
#         hide eza

#         show imen talking at left
#         imen "Good luck with that! I'm sure you'll do great!"
#         hide imen

#         narrator "{i}You and Imen part ways and you head home.{/i}"

#         narrator "{i}As the saying goes, there is no rest for the wicked. Once you get back home you're back on the CSC 110 grind.{/i}"

#     else:
#         narrator "{i}Stepping out of the class you feel drained. All you can do is hope that what you put out there was enough.{/i}"

#         narrator "{i}Even though your exhuasted, you still have CSC 110 to study for. There is no rest for the wicked. Once you get back home, 
#         you're back on the CSC 110 grind.{/i}"

#     call loading
#     jump write_csc110_midterm

#     ##############################################################################################
#     #write_csc110_midterm
#     ##############################################################################################

#     label write_csc110_midterm:

#         scene night with dissolve 
        
#         narrator "{i}It's the day of the midterm and you and Angus have agreed to meet in the library before going to the exam room together.
#         You think that the exam being outside of class time is absured.{/i}"
        
#         narrator "{i}Having to come back to campus for 7:00PM, is exhuasting. Especially
#         since you had class earlier this morning.{/i}"

#         narrator "{i}While you were at home you did some last minute review. During that review, you realized that you completly don't understand
#             loops, neither for or while loops.{/i}"

#         if (went_to_office_hours):
#             narrator "{i} This was what Dr. Berg was trying to explain in office hours, but you were to panicked to absord anything.{/i}"
        
#         menu:
#             "You know you're going to see Angus before the midterm, do you ask him for help or not?"

#             "Ask him for help":
#                 $ academic_points += 0
#                 $ will_to_survive_points += 0
#                 $ relationship_points += 5

#                 narrator "{i}You decide to ask him for help, as soon as you see him in the library you pull out your ipad.{/i}"

#                 show eza stressed at right
#                 eza "I don't understand loops?"
#                 hide eza 

#                 show angus neutral at left
#                 angus "What do you mean, didn't you do the assignment?"
#                 hide angus

#                 show eza stressed at right
#                 eza "I somehow did the assignment without understanding them."
#                 hide eza 

#                 show angus neutral at left
#                 angus "Okay, let's go over this."
#                 hide angus

#                 narrator "{i}Angus gives you a crash course on for, while, and nested loops in 15 minutes. You just hope that whatever he said sticks.{/i}"
            
#             "Don't ask him for help":

#                 $ academic_points -= 0
#                 $ will_to_survive_points -= 0
#                 $ relationship_points -= 5

#                 narrator "{i}You decide to just go with what you know. By the time you make it to the library there's not going to be enough time to actually
#                 learn anything.{/i}"

#                 scene library with dissolve

#                 narrator "{i}With extra time you have before the midterm, you meet up with Angus at the library, and the two of you 
#                 chill for a bit before heading out.{/i}"
    
#         scene night time school yard with dissolve

#         narrator "{i}The two of head over to the Engineering and Computer Science Building. The hallway outside the lecture hall is filled with stressed out students.
#         The claustrophbic hot atmosphere does nothing for your nerves.{/i}"

#         scene lecture hall with dissolve 
#         narrator "{i}Soon 200 students are let into the lecture hall and the two of you sit down to write the test.{/i}"

#         narrator "{i}Once everyone is situated Dr Berg begins speaking.{/i}"

#         show celina talking at left

#         celina "Some notes before you get started, this is a 50 minute midterm and there are 6 questions to answer. Since there are so many of you, we will not be answering 
#         questions."
        
#         celina "If you have a question, write down you're assumption and if it is reasonable, we will take it into consideration when marking your test."

#         celina "For a lot of you, this might be the first midterm you've ever taken in university. So I understand that there may be a lot of nerves tonight. 
#         But, you guys have studied hard for this. I am sure everything is going to be okay."

#         hide celina

#         narrator "{i}There are two minutes left on the clock.{/i}"

#         show celina talking at left
#         celina "You may as soon as the clock hits 7:00PM. Good luck everyone!"
#         hide celina

#         narrator "{i}As soon as the clock hits 7, there is a great rustle of paper.{/i}"

#         narrator "{i}As soon as you open the test's cover everything that you studied leaves your brain. There's so much documentation, and even though you practiced writing code, 
#         the format is completly unfamilliar.{/i}"

#         scene black with dissolve 

#         narrator "{i}First page, you can't answer anything... you flip the page.{/i}"

#         narrator "{i}Second page, you can't answer anything... you flip the page.{/i}"

#         narrator "{i}Third page, you can't answer anything... you flip the page.{/i}"

#         narrator "{i}Fourth page, no answer pops out to any of the questions... you flip the page.{/i}"

#         narrator "{i}Fifth page, you can't answer anything... you flip the page.{/i}"
        
#         narrator "{i}Sixth page, you can't answer anything... you flip the page.{/i}"

#         narrator "{i}You've made it to the end of the test...{/i}"

#         call loading 

#         jump s1t1_ending

#     # narrator "{i}{/i}"
#     ##############################################################################################
#     #s1t1_ending
#     ##############################################################################################
#     # narrator "{i}{/i}"

#     label s1t1_ending:

#         scene black with dissolve 

#         narrator "{i}You've got through the first set of midterms for this semester.{/i}"

#         narrator "{i}You're absolulty exhausted, you want to sleep and never wake up again.{/i}"

#         narrator "{i}The hour is late, it's dark and raining hard outside. You're still at school in the Engineering and Computer Science building
#         working through your other assignment, when suddenly, you get consecutive notifications on your phone.{/i}"

#         narrator "{i}CSC110 Nofitication: Grades released for midterm 1...{/i}"

#         narrator "{i}MATH122 Notification: Grades for midterm 1...{/i}"

#         narrator "{i}You're heart is pounding, you're not sure if you want to look at the grades or not.{/i}"

#         narrator "{i}Deciding not to push the enivitable you open up your laptop and look at the grades.{/i}"

#         narrator "{i}You look at the Math 122 marks first.{/i}"

#         if met_imen and has_tutor:

#             $ academic_points -=  5
#             $ will_to_survive_points -= 10
#             $ relationship_points += 0

#             narrator "{i}You got a 60%% on the midterm. It's not the best, and you're not happy at yourself for it, but a pass is a pass.
#             An engineering and computer science pass nonetheless.{/i}"

#             narrator "{i}With all the work that you did and the help that you got, this was the best you could do.{/i}"

#             narrator "{i}With a sigh you accept your result. It is what it is. You're just going to have to make it up in the 
#             next midterm.{/i}"

#         elif (met_imen and not has_tutor) or (not met_imen and has_tutor):

#             $ academic_points -= 10
#             $ will_to_survive_points -= 15
#             $ relationship_points += 0

#             narrator "{i}You got a 50%% on the midterm. It's not the best, you expected better. It's not even enough to be considered an
#             engineering and computer science pass.{/i}"

#             narrator "{i}With all the work that you did and the help that you got, this was the best you could do.{/i}"

#             narrator "{i}With a sigh you accept your result. It is what it is. You're just going to have to make it up in the 
#             next midterm.{/i}"

#         else:

#             $ academic_points -= 15
#             $ will_to_survive_points -= 20
#             $ relationship_points += 0

#             narrator "{i}You got a 45%% on the midterm.{/i}"

#             narrator "{i}You feel like you should cry and be upset, but all you feel is numbness. All those negative thoughts that you
#             have had all semester seem to be real.{/i}"

#         narrator "{i}With a heavy heart you change tabs and look at the CSC 110 marks next.{/i}"

#         $ academic_points -= 5
#         $ will_to_survive_points -= 5
#         $ relationship_points += 0

#         narrator "{i}60%%.{/i}"

#         narrator "{i}It's a pass. What more can you want at this point.{/i}"

#         call loading

#         if (academic_points > 60 and will_to_survive_points > 70 and relationship_points > 50):

#             scene black with dissolve

#             narrator "{i}You're not happy with the mark, but you're not upset either. You're just glad that you passed.{/i}"

#             call loading 

#             scene level cleared with dissolve

#             narrator "{i}Congratulations! You have lived to survive another day.{/i}"

#             narrator "{i}Let's see do you have the will to complete another semester?{/i}"

#             return

#         else:

#             scene black with dissolve

#             narrator "{i}You're not sure what to do. You're not sure if you can do this. You're not sure if you want to do this.{/i}"

#             narrator "{i}No, you don't want to do this anymore...{/i}"

#             scene bad ending with dissolve

#             narrator "{i}Unfortunatly, this is end.{/i}"
#             return


#     ##############################################################################################
#     #loading
#     ##############################################################################################

#     label loading:
#         scene black
#         show text "Loading..." with Pause(3, Hard=True)
#         return

#     return
