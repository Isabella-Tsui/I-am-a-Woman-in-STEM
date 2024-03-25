##################################################################################################

#Characters #####################################################################################

define narrator = Character("")

define isla = Character("Isla")

define khashvi = Character("Khashvi")

define andrew = Character("Andrew")

define imen = Character("Imen")

define drBankole = Character("Dr. Bankole")

define emma = Character("Dr. Hones")

#Regular Points ##################################################################################

default academic_points = 80
default will_to_survive_points = 80
default relationship_points = 50 

#Booleans ########################################################################################

default met_imen = False
default has_tutor = False
default went_to_office_hours = False

##################################################################################################


label start:

        jump intro

        ##############################################################################################
        #intro
        ##############################################################################################
        label intro:

                scene summer with dissolve 
            
                narrator "Summer has come to an end and Isla is preparing to start her first year at the University of Victoria City.\n\n
                (Click the track pad or mouse to move forward in the story)"

                narrator "In a spur-of-the-moment  decision over the summer, Isla decided to transfer from the business\
                program into computer science."

                narrator "Despite knowing very little about it and having never taken a comp science course in her life, she has decide
                to commit to her decision and go into the next chapter of her life."

                narrator "Your job is to help Isla make choices and navigate through her 4 year journey."

                show screen game_stats

                narrator "The choices you make will affect Isla's academics, mental and physical health, and relationships. Isla\
                needs a certain amount of each category to function as a decent human being and to proceed to the next year."

                narrator "Depending on your choices, you can also get win bonus points. "

                $ renpy.notify("+1 points for starting the game")
                $ will_to_survive_points += 1

                narrator "The addition of bonus points look like this"

                narrator "Hopefully, you make enough right choices so that Isla can graduate with a degree in computer science. Good luck!"
                
                call loading 

                jump night_before_orientation
        
        ##############################################################################################
        #night_before_orientation
        ##############################################################################################
        label night_before_orientation:

                scene bedroom with dissolve

                narrator "{i}You're sitting in your room texting your friend, Khashvi, who is also starting university.{/i}"

                narrator "{i}You're trying to ignore it, but the nerves are beginning to settle in. After taking a year off to work,
                all your friends from high school are ahead, and it feels like you're completely starting over.{/i}"

                scene texting on phone with dissolve

                show khashvi talking at left
                narrator "From Khashvi: Hey how are u feeling about school?"
                hide khashvi

                show isla talking at right
                narrator "From Isla: Worried I'm going to get lost but what's new lol"
                hide isla

                show khashvi talking at left
                narrator "From Khashvi: I'll probably still get lost even though we walked to our classes the other day"
                hide khashvi
                
                show khashvi talking at left
                narrator "From Khashvi: Are going to the orientation event tomorrow?"
                hide khashvi

                show isla talking at right
                narrator "From Isla: I was thinking about it"
                hide isla
                
                show isla talking at right
                narrator "From Isla: Were you planning on going?"
                hide isla

                show khashvi talking at left     
                narrator "From Khashvi: Yeah I think it's a good idea to go"
                hide khashvi

                menu: 
                        "Should Isla go to the event?"
                        "Yes" :
                                $ relationship_points += 5

                                show isla talking at right
                                narrator "From Isla: Yeah I'd think it would be a good idea"
                                hide isla

                                show isla talking at right
                                narrator "From Isla: I'll meet you there?"
                                hide isla

                                show khashvi talking at left
                                narrator "From Khashvi: Yeah I'll see you there"
                                hide khashvi

                                call loading
                                jump orientation_day_good_ending

                        "No" :
                                $ relationship_points -= 5

                                show isla talking at right
                                narrator "From Isla: I don't think I'll be going"
                                hide isla

                                show isla talking at right
                                narrator "From Isla: have fun tho"
                                hide isla 

                                show khashvi talking at left
                                narrator "From Khashvi: Thanks! I'll tell you how it goes"
                                hide khashvi

                                call loading
                                jump orientation_day_bad_ending


        
        ##############################################################################################
        #orientation_day_good_ending
        ##############################################################################################

        label orientation_day_good_ending:

                scene bus stop with dissolve 

                narrator "{i}You've made it to school without a hitch. The air is warm; you're sitting on a bench under 
                the shade, listening to Lana del Rey as you wait for Khashvi.{/i}"

                narrator "{i}Looking at your phone, you see that there are 15 minutes to the event, 
                it takes 10 minutes to walk across campus, and Khashvi isn't here yet.{/i}"

                narrator "{i}You realize she won't make it in time, and shoot her a text.{/i}"

                scene texting on phone with dissolve
                
                show isla talking at right
                narrator "From Isla: Hey do you want me to wait for u?"
                hide isla

                show khashvi talking at left
                narrator "From Khashvi: No it's okay I'm not going to make it in time"
                hide khashvi

                show khashvi talking at left
                narrator "From Khashvi: I'll see u later!"
                hide khashvi

                show isla talking at right
                narrator "From Isla: Okay see u later"
                hide isla

                scene courtyard with dissolve

                narrator "{i}You're a bit anxious about going without your friend, but you walk to the Engineering and Computer Science building (ECS)\ 
                and try to get situated.{/i}"

                narrator "{i}The lady running registration asks for your name and hands you a name tag. She lets you know what group your in, you thank her, and try to find\
                these people.{/i}"

                narrator "{i}You find the group and sit down. Slowly, the group grows to a considerable size. You don't think that you'll be able to form any close relationships,
                but you'll try.{/i}"

                narrator "{i}You're all trying to figure out how to color in the team logo, and they include you because you briefly mentioned that you have done some art\
                before. After finishing the logo, your team is directed to go do the activities.{/i}" 

                scene lecture hall with dissolve

                narrator "{i}The team lead brings your group into a large lecture hall. All around you are robotics materials spread out on tables.
                There's even a makeshift racetrack at the front.{/i}"

                narrator "{i}You try to participate, but there are so many people in the group, and you don't have any experience building or programming robots,
                so you mostly end up watching.{/i}"

                scene courtyard with dissolve

                narrator "{i}The rest of the morning goes in a similar manner, changing activities every couple of hours. Eventually, your team is led back to the meeting area,
                where a pizza lunch is distributed to everyone. You text Khashvi to see where she is but get no reply.{/i}"

                menu:
                        "You see small groups of girls scattered about, do you go talk to one of them?"
                        "Yes talk to them" :
                                $ relationship_points += 5
                                $ will_to_survive_points -= 5

                                narrator "{i}You walk over to a group and say hi. They're all in different programs and out of town, so it's harder to find something in common\
                                to talk about. Since you live at home, you can't relate to being in res or the struggle of moving to a new city.{/i}"

                                narrator "{i}Over the lunch break, you go around talking to different groups. You're able to exchange information with some cool German exchange students.
                                It's all small talk, nothing that your old job in customer service couldn't have prepared you for.{/i}"

                        "No don't talk to them" :
                                $ will_to_survive_points += 5

                                narrator "{i}You decide to find a nice spot in the shade and eat your pizza. There's been a lot of interactions all day, and you've been around more people 
                                in one day than you have all summer. You know that you should probably socialize, so you tell yourself that you'll do it tomorrow.{/i}"

                scene courtyard2 with dissolve

                narrator "{i}After being unsuccessful in finding your group after lunch, you end up running into Khashvi. Here, you are introduced to a new friend, Andrew, whom
                Khashvi made while she was doing the activities with her team.{/i}"

                show khashvi talking at left
                khashvi "Hey Isla, how was your day?"
                hide khashvi talking

                show isla talking at right
                isla "Not too eventful, we built a lego version of the quad and built a robot. How about you guys?"
                hide isla talking

                show khashvi talking at left
                khashvi "Our team kind of took over haha. We've just been hanging out while they've been doing the activities."

                khashvi "This is Andrew by the way."
                hide khashvi talking

                show andrew talking at left
                andrew "Hey, nice to meet you."
                hide andrew talking

                show isla talking at right
                isla "Nice to meet you too. What program are you in?"
                hide isla talking

                show andrew talking at left
                andrew "I'm in computer science."
                hide andrew talking

                show isla talking at right
                isla "Cool, me too!"
                hide isla talking

                narrator "{i}Since you took a gap year, all your high school friends besides Khashvi are ahead. Because Khashvi is in SEng, you weren't going to be in the same
                classes, so knowing someone else and being in the same class as them is relieving to hear.{/i}"
                
                narrator "{i}You and Andrew end up trading phone numbers and comparing schedules. You both notice that you are in the same CSC 110 course.{/i}"

                narrator "{i}After seeing that, the two of you agree to meet up and go to lecture together tomorrow.{/i}"

                scene lecture hall with dissolve

                narrator "{i}Since you lost your group, you assimilated into Andrew and Khashvi's team. The groups are so big that no one really notices that
                you joined. The team ends up in a lecture hall where the teams are tallying points from the activities.{/i}"

                narrator "{i}Each team leader stands, and the president of the Engineering department, Jessica, calls out numbers like it's a bid \"10...20...30...40...
                80...90...100...\"{/i}"

                narrator "{i}Slowly team leads sit down until one is left \"...120 going once, going twice, we have a winner!\"{/i}"
                
                show khashvi talking at left
                khashvi "{i}That's our team lead standing up.{/i}"
                hide khashvi talking

                show andrew talking at left
                andrew "{i}Looks like it is.{/i}"
                hide andrew talking

                show khashvi talking at left
                khashvi "{i}I wasn't expecting that to happen. Good thing you lost your team too.{/i}"
                hide khashvi talking

                show isla talking at right
                khashvi "{i}I guess it is.{/i}"
                hide isla talking

                scene sunset with dissolve

                narrator "{i}The president takes the team into one of the engineering buildings and hands out sweatshirts and hoodies to the team.{/i}"

                narrator "{i}The day's activities are over, and the three of you head off to the bus stop after a relatively enjoyable day.{/i}"

                $ renpy.notify("+2 points for having a good day and making friends")
                $ will_to_survive_points += 1
                $ relationship_points += 1
                
                call loading
                jump first_day_good_ending

        ##############################################################################################
        #orientation_day_bad_ending
        ##############################################################################################

        label orientation_day_bad_ending:

                scene bedroom with dissolve

                narrator "{i}You're sitting in your room thinking about the event that you didn't go to. You decide not to think about it too deeply and\ 
                enjoy the last day of summer. You make an iced coffee before going outside and cracking open a manga.{/i}"

                narrator "{i}You spend the day reading and soaking up the last of the summer sun.{/i}"
                
                narrator "{i}In the evening, you receive a text from Khashvi.{/i}"

                scene texting on phone with dissolve
                
                show khashvi talking at left
                narrator "From Khashvi: Hey how was your day?"
                hide khashvi

                show isla talking at right
                narrator "From Isla: It was good I spent the day outside"
                hide isla

                show khashvi talking at left
                narrator "From Khashvi: That's nice"
                hide khashvi

                show khashvi talking at left
                narrator "From Khashvi: I went to the orientation event today"
                hide khashvi

                show khashvi talking at left
                narrator "From Khashvi:  It was fun I met a guy named Andrew."
                hide khashvi
                
                show khashvi talking at left
                narrator "From Khashvi: He's in computer science"
                hide khashvi

                show khashvi talking at left
                narrator "From Khashvi: I think you would like him"
                hide khashvi

                show isla talking at right
                narrator "From Isla: That's cool I'm glad you had fun!"
                hide isla

                show khashvi talking at left
                narrator "From Khashvi: Yeah there were some activities and we won a prize"
                hide khashvi

                show khashvi talking at left
                narrator "From Khashvi:  I can't wait to tell you about it tomorrow"
                hide khashvi

                show isla talking at right
                narrator "From Isla: Can't wait to hear about it!"
                hide isla

                $renpy.notify("+1 points for having a good day")
                pause 3
                $ will_to_survive_points += 1
                
                scene black with dissolve
                
                call loading 
                jump first_day_bad_ending

        ##############################################################################################
        #first_day_good_ending
        ##############################################################################################

        label first_day_good_ending:

                scene hallway with dissolve

                narrator "{i}Thankfully, you did a walkthrough of the campus with Khashvi the other day, so you're able to find your first class right away.
                Standing outside the door, you catch a familiar glimpse of blonde hair.{/i}"

                show isla talking at right
                isla "Hey Andrew, how you doing?"
                hide isla

                show andrew talking at left
                andrew "Pretty good, what about you?"
                hide andrew

                show isla talking at right
                isla "I'm doing alright."
                hide isla

                scene lecture hall with dissolve

                narrator "{i}The two of you head into the lecture hall and find a seat in the middle. After coming back from the pandemic,
                it's a bit overwhelming to see 200 students in one space.{/i}"

                narrator "{i}Soon, the professor, Dr. Emma Hones, comes in and starts talking about the course and the syllabus.{/i}"

                show emma talking at left
                emma "Good morning everyone! I'm Dr. Hones and I'll be your professor for CSC 110."

                emma "I want to get to some programming today so I'm going to quickly go over the syllabus."

                emma "Everything you need to know is on the course website, so make sure to check it out."

                emma "In this class there are weekly assignments and labs, pre-lecture videos and quizzes, and of course midterms and a final..."
                hide emma 

                narrator "{i}Soon, Dr. Hones finishes the housekeeping and starts going over some programming concepts. She encourages everyone to program along.{/i}"

                scene laptop with dissolve 

                narrator "{i}You pull out your laptop and enter the password; after a moment, you read that the password is incorrect. You try again and again, but it's not working.{/i}"

                narrator "{i}You feel like a joke, why can't you remember what your password is. No to mention, this is your first time owning a laptop.{/i}"
                
                narrator "{i}Even though they're probably not, you hope that the people behind you don't see you struggle. As you try to figure out your password,
                Dr. Hones is moving on with her demo.{/i}"  

                menu:
                        "What do you do? Do you keep trying? Do you ask Andrew if you can follow along with what he's doing?"
                        
                        "Ask Andrew":

                                $ relationship_points += 5
                                $ academic_points += 5
                                $ will_to_survive_points -= 5

                                narrator "{i}You lean over to Andrew and ask if you can follow along with what he's doing.{/i}"

                                show isla talking at right
                                isla "Hey, would you mind if I follow along with what you're doing?"
                                hide isla

                                show andrew talking at left
                                andrew "Yeah, for sure."
                                hide andrew talking

                                narrator "{i}As you watch Andrew and Dr. Hones program, questions keep coming to your head.{/i}"

                                narrator "{i}She's talking about a function, what is a function? What is this \"foo\" that she's talking about?{/i}"

                                narrator "{i}Nothing really makes sense, and you're confused as to what's going on.{/i}"

                                narrator "{i}This is supposed to be an introduction to computer science, why doesn't it feel that way?{/i}"

                                $ renpy.notify("+1 points for trying")
                                $ academic_points += 1
                                pause 3

                        "Keep trying to figure out the password":

                                $ academic_points -= 5
                                $ will_to_survive_points -= 10

                                narrator "{i}You keep trying to figure out the password, but you're not able to get it.{/i}"

                                narrator "{i}You feel pathetic and overwhelmed for not being able to figure out something so simple.
                                You end up being so wrapped up that you can't hear what Dr. Hones is saying.{/i}"

                                narrator "{i}You keep trying until you MacBook disables itself.{/i}"
                                
                                narrator "{i}Behind you, there are two boys. Even though they're trying to whisper, you can hear them saying,
                                \"What's a girl like her doing in this class? She doesn't belong here.\"{/i}"

                                narrator "{i}You know you're not the only one who heard their comments because Andrew turns and gives you a sympathetic look.{/i}"

                                narrator "{i}The tips of your ears burn red and tears sting behind your eyes.{/i}"

                                narrator "{i}What are you even doing here? You can't even get your MacBook to work. How are you supposed to be a computer scientist?{/i}"
                                
                                call loading
                scene laptop with dissolve

                narrator "{i}You end up trying your password one more time before class finishes. With an exasperated sigh, you see that it works.
                You swear to God you've tried that one before.{/i}"

                scene lecture hall with dissolve
                
                narrator "{i}Class ends, and you and Andrew pack up and head out of the lecture hall to meet with Khashvi.{/i}"

                call loading
                jump school_schedule


        ##############################################################################################
        #first_day_bad_ending
        ##############################################################################################

        label first_day_bad_ending:

                scene lecture hall with dissolve

                narrator "{i}Thankfully, you did a walkthrough with Khashvi the other day, so you can find your first class right away.
                Entering the class, you feel a bit overwhelmed.{/i}"

                narrator "{i}There isn't anyone in the room that looks familiar, and coming back from the pandemic, it's a bit overwhelming being around 200 plus students.
                Quickly, you look for an empty seat and sit down.{/i}"

                narrator "{i}The professor, Dr. Hones, comes in and starts talking about the course and the syllabus.{/i}"
                
                show emma talking at left
                emma "Good morning everyone! I'm Dr. Hones and I'll be your professor for CSC 110."

                emma "I want to get to some programming today so I'm going to quickly go over the syllabus."

                emma "Everything you need to know is on the course website, so make sure to check it out."

                emma "In this class there are weekly assignments and labs, pre-lecture videos and quizzes, and of course midterms and a final..."
                hide emma 

                narrator "{i}Soon, Dr. Hones finishes the housekeeping and starts going over some programming concepts. She encourages everyone to program along.{/i}"
                
                scene laptop with dissolve

                narrator "{i}You pull out your laptop and enter the password; after a moment, you read that the password is incorrect. You try again and again, but it's not working.{/i}"

                narrator "{i}You feel like a joke, why can't you remember what your password is. No to mention, this is your first time owning a laptop.{/i}"
                
                narrator "{i}Even though they're probably not, you hope that the people behind you don't see you struggle. As you try to figure out your password,
                Dr. Hones is moving on with her demo.{/i}"

                menu:
                        "What do you do? Do you sit and try to focus on the lecture without doing the exercise? Or try to fix the laptop?"
                        
                        "Sit there and try to focus on the lecture":

                                $ academic_points -= 5
                                $ will_to_survive_points -= 5

                                scene lecture hall with dissolve

                                narrator "{i}You close the laptop and try your best to focus on what Dr. Hones is saying.{/i}"

                                narrator "{i}As you watch her program and explain basic concepts, questions keep coming to your head.{/i}"

                                narrator "{i}She's talking about a function, what is a function? What is this \"foo\" that she's talking about?{/i}"

                                narrator "{i}Nothing really makes sense, and you're confused with what's going on.{/i}"

                                narrator "{i}This is supposed to be an introduction to computer science, why doesn't it feel that way?{/i}"

                        "Try to fix the laptop":

                                $ academic_points -= 5
                                $ will_to_survive_points -= 10

                                narrator "{i}You keep trying to figure out the password, but you're not able to get it.{/i}"

                                narrator "{i}You feel pathetic and overwhelmed for not being able to figure out something so simple.
                                You end up being so wrapped up that you can't hear what Dr. Hones is saying.{/i}"

                                narrator "{i}You keep trying until you MacBook disables itself.{/i}"
                                
                                narrator "{i}Behind you, there are two boys. Even though they're trying to whisper, you can hear them saying,
                                \"What's a girl like her doing in this class? She doesn't belong here.\"{/i}"

                                narrator "{i}The tips of your ears burn red and tears sting behind your eyes.{/i}"

                                narrator "{i}What are you even doing here? You can't even get your MacBook to work. How are you supposed to be a computer scientist?{/i}"
                
                scene laptop with dissolve

                narrator "{i}You end up trying your password one more time before class finishes. With an exasperated sigh, you see that it works.\
                You swear to God that you've tried that one before.{/i}"

                scene lecture hall with dissolve
                
                narrator "{i}When class ends, you pack up and head out of the lecture hall to meet with Khashvi.{/i}"

                call loading 

                scene courtyard2 with dissolve

                narrator "{i}As you walk up to Khashvi, you notice a blonde haired boy beside her.{/i}"

                show khashvi talking at left
                show andrew talking at right
                khashvi "Hey Isla, this is Andrew. He's in computer science too."
                hide khashvi 

                show andrew talking at left
                andrew "Hey, nice to meet you."
                hide andrew

                show isla talking at right
                isla "Nice to meet you too!"
                hide isla 

                narrator "{i}The three of you have lunch and talk about orientation day and the first day of class.{/i}"
                
                narrator "{i}Apparently, Khashvi met Andrew during orientation, and they became good friends over the course of the day.
                Andrew seems really nice; it's easy to talk and joke around with him.{/i}"

                narrator "{i}The two of you also happen to be in the same CSC 110 class. Over the lunch period, you and Andrew both
                agree that the next time you have class, the two of you should meet up and sit together.{/i}"

                call loading
                jump school_schedule

        ##############################################################################################
        #school_schedule
        ##############################################################################################

        label school_schedule:

                scene street night with dissolve 

                narrator "{i}You start getting into the swing of things. You're able to find your classes and create some semblance of a routine.
                You're taking Math 122, CSC 110, FRAN 170, and ENGL 142.{/i}"

                narrator "{i}After the initial excitement of starting at a new school wears away, everything begins to feel monotonous.{/i}"

                narrator "{i}Wake up at 6:30 AM{/i}"
                narrator "{i}Get dressed{/i}"
                narrator "{i}Take the bus before the sun rises{/i}"
                narrator "{i}Go to your 8:30 AM class{/i}"
                narrator "{i}Study with Andrew until Math 122{/i}"
                narrator "{i}Have lunch alone{/i}"
                narrator "{i}Go to French{/i}"
                narrator "{i}Go home when it's dark{/i}"
                narrator "{i}Eat{/i}"
                narrator "{i}Do homework{/i}"
                narrator "{i}Go to bed{/i}"
                narrator "{i}Repeat{/i}"

                narrator "{i}You're not sure what you're doing, but you're doing it. You're not sure if you're happy, but you're not sad either.
                You're just kind of there, and you're not sure if you're okay with that.{/i}"

                call loading
                
                scene math class with dissolve

                narrator "{i}French and English classes are going well, but you're struggling with math and computer science. You're not sure what's going on.
                At least with computer science, you can make it through with trial and error. But with math, it feels like it's not even doing math anymore.{/i}"

                narrator "{i}When your professor started going on about logical implications you lost it.{/i}"

                narrator "{i}A true and a true imply a true; okay, that makes sense to me. A false and a false implying a false; I can see that.
                A truth and a false make a truth ALWAYS?! How?!{/i}"

                narrator "{i}Everyone except for you seems to know what they're doing. The people who can talk back to the professor are terrifying.
                The level of intelligence that they have to grasp these things so quickly is astonishing.{/i}"

                narrator "{i}Math 122 has just finished, and you're sitting with your laptop open. The grades for the last assignment have just come out.{/i}"

                narrator "{i}You have barely managed to scrape through with a 50%%.{/i}"
                $ academic_points -= 5
                $ will_to_survive_points -= 5

                narrator "{i}This makes you freeze, you've never got less than 70%% on your assignments before. This is the first assignment for this class.\
                It can only get harder from here.{/i}"

                menu:
                        "Do you decide to reach out to your professor for help or not?"

                        "Yes, get help":
                                narrator "{i}You feel absolutely gutted. Your stomach has a stone in it, your heart is your throat, and you're doing everything in your\
                                power to keep the tears at bay.{/i}"

                                narrator "{i}You take some breaths and focus on packing up. You leave the classroom and find a quite space to have a Zoom meeting. You wait,\
                                contemplating the choices that got you to this place.{/i}"

                                call loading

                                scene myanhardt office with dissolve

                                narrator "{i}Office hours start, and you jump on the Zoom link. You wait until everyone is done before you request to talk privately in a breakout room.{/i}"

                                narrator "{i}The two of you go over your assignment; you know the things you got wrong were just things you didn't know. But then she asks you\
                                something unexpected.{/i}"

                                show drBankole talking at left
                                drBankole "{i}Do you have any friends in this class?{/i}"
                                hide drBankole 

                                narrator "{i}You're taken aback by the question.{/i}"

                                show isla indifferent at left
                                isla "Yes...I have a friend in this class."
                                hide isla

                                narrator "{i}Even though that's clearly a lie{/i}"

                                show drBankole talking at left
                                drBankole "{i}I think it would be a good idea to form a study group with them. I think that would be beneficial for you..."
                                hide drBankole talking

                                narrator "{i}The conversation ends soon after.{/i}"

                                narrator "{i}It wasn't super helpful. However, in hindsight, the world didn't end when you asked for help.{/i}"

                                $ will_to_survive_points += 5
                                $ relationship_points += 5

                                narrator "{i}After office hours, you decide that enough is enough. If you need assistance, you need assistance.\
                                There's nothing wrong or shameful in needing help.{/i}"

                                scene masc with dissolve

                                narrator "{i}As soon as you find the time, you go to the math and stats assistance center to ask for help. With renewed determination\
                                and questions in mind, you put yourself down on the waitlist.{/i}"

                                narrator "{i}Soon, you meet with a tutor but realize that their teaching style is not for you.
                                While you have a better understanding of what you need to do, you need more help and time to understand the concepts.{/i}"

                                $ renpy.notify("+1 points for trying")
                                $ academic_points += 1
                                pause 3 

                                menu:
                                        "Do you find an outside tutor?"
                                        "Yes":
                                                call loading
                                                jump find_a_tutor_good_ending
                                        "No":
                                                call loading
                                                jump find_a_tutor_bad_ending
                                
                        "No, don't get help":

                                scene bus stop with dissolve

                                narrator "{i}You pack up as fast as you can. The blood is rushing to your ears, and all you can think about is getting home as fast as possible.
                                The weight in your stomach grows, and all you can do is hope to keep your emotions in check until you get home.{/i}"

                                $ academic_points -= 5
                                $ will_to_survive_points -= 10

                                scene bedroom with dissolve 

                                narrator "{i}You get home, and you're able to keep it together until you get to your room. You close the door and let the tears fall.{/i}"

                                narrator "{i}You cry not just because of the homework but everything else that's going on.
                                The proverbial bucket has filled and is now spilling all over the floor.{/i}"

                                narrator "{i}After your tears have run dry, you pick yourself up and decide to take a look at the next math assignment. It really doesn't look any better than the first,
                                but you sit yourself down and try to take a crack at it.{/i}"

                                call loading

                                scene desk with dissolve
                            
                                narrator "{i}After hours of screening through your notes, textbook, and examples, there's nothing but the question number on your paper.
                                With a deep sigh, you close your books and head to bed.{/i}"

                                narrator "{i}This trend continues; days pass, and you're getting closer and closer to the deadline.{/i}"

                                narrator "{i}After another unsuccessful study session, in bed, you think to yourself, \"I can\'t let this go on any further\".{/i}"

                                call loading

                scene masc with dissolve

                narrator "{i}The next day, you go to the math and stats assistance center to ask for help. With renewed determination and questions in mind, you put\
                yourself down on the wait list.{/i}"

                narrator "{i}Soon, you meet with a tutor but realize their teaching style is not for you. While you have a better understanding of what they're saying,
                you need more help and time to understand the concepts.{/i}"

                narrator "{i}You decide to try again with another tutor, but the same thing happens. This cycle continues until the math and stats center closes.{/i}"

                narrator "{i}Afterwards, you go home and turn in whatever work you have. You're completely unsatisfied with the work you've done, and the time you've spent on this class.{/i}"

                call loading 
                jump mental_health_talk

        ##############################################################################################
        #find_a_tutor_good_ending
        ##############################################################################################

        label find_a_tutor_good_ending:

                scene math tutoring with dissolve

                $ will_to_survive_points += 5
                $ academic_points += 5
                $ relationship_points += 5
                
                narrator "{i}After being unsuccessful at the math and stats help center, you go looking for external help. You go online and look for a math tutor in your area.
                You come across one man, Ryan, and reach out to him for help{/i}."

                narrator "{i}You meet with him, and he's able to help you understand the concepts that you're struggling with.{/i}"

                narrator "{i}You're able to get the help that you need, and you leave the tutoring session feeling a lot better about what you're doing at school. 
                Fortunately, some of that pressure has been lifted.{/i}"

                call loading 
                jump find_friends_in_math122

        ##############################################################################################
        #find_a_tutor_bad_ending
        ##############################################################################################

        label find_a_tutor_bad_ending:

                scene masc with dissolve

                $ will_to_survive_points -= 5
                $ academic_points -= 5

                narrator "{i}You decide against finding a tutor; they're expensive, and you don't know if there are people capable of helping you with this kind of material.
                As a result, you continue to go to the math and stats assistance center.{/i}"

                narrator "{i}You go several times a week, but you get the same outcome each time. You leave half understanding what you came to understand.{/i}"

                narrator "{i}It feels disheartening. You're trying your best, and so are the tutors, but nothing seems to click 100%%{/i}"
                
                scene black with dissolve

                call loading
                jump find_friends_in_math122

        ##############################################################################################
        #find_friends_in_math122
        ##############################################################################################

        label find_friends_in_math122:

                scene math class with dissolve

                narrator "{i}Stepping into Math 122, you recall the first time you had this class. You came early, and there weren't that many people there at first.
                However, as the start time approached, you noticed seats filled with more men than women.{/i}"
                
                narrator "{i}Of the few women who entered the class, there was one who didn't seem to already be in a friend group.{/i}"

                narrator "{i}You see that girl again sitting next to some boy.{/i}"

                menu:
                        "Do you go sit next to her?"
                        "Yes":
                                $ relationship_points += 5
                                $ will_to_survive_points += 5

                                narrator "{i}You walk over to her and sit down. You introduce yourself and she does the same.{/i}"

                                show isla talking at right
                                isla "Hey, I'm Isla."
                                hide isla 

                                show imen talking at left
                                imen "Hi, I'm Imen."
                                hide imen

                                narrator "{i}The two of you exchange small talk until Dr. Bankole begins her lesson. At the end of class, the two of you exchange your\
                                goodbyes and you hope that you can kindle this friendship.{/i}"
                                $ met_imen = True

                                $renpy.notify("+1 points for going out of your comfort zone")
                                $ will_to_survive_points += 1
                                pause 3

                                scene black with dissolve

                                call loading
                                jump mental_health_talk

                        "No":
                                $ relationship_points -= 5
                                $ will_to_survive_points -= 5
                    
                                narrator "{i}As more people filter in and sit down around her, it seems like she already has an established friend group. Feeling shy, you decide to sit in the same\
                                spot as you always do.{/i}"

                                narrator "{i}Immediately after sitting down, you regret not going up there. Because even if you didn't talk, at least you tried.{/i}"

                                call loading
                                jump mental_health_talk

        ##############################################################################################
        #mental_health_talk
        ##############################################################################################

        label mental_health_talk:

                scene kitchen with dissolve 

                narrator "{i}Since university has started, your mental health has slowly declined. The constant stress of deadlines has your motivation flagging,\
                you've been in a haze for what feels like ages, and it seems like you're just going through the motions of life.{/i}"

                narrator "{i}It doesn't feel like you're living. Aren't your twenties supposed to be the best time of your life?{/i}"

                narrator "{i}You're in the kitchen making spicy fire noodles when your mom walks in. She asks how you're doing, and you don't know how to respond.{/i}"

                menu:
                        "Do you tell her you're not doing fine? Or do you lie?"
                        "Tell her you're not doing fine":

                                $ will_to_survive_points -= 5
                                $ relationship_points += 5

                                show isla anxious at right
                                isla "I'm not doing well. There's so much going on, and I don't know how to handle it."
                                isla "I'm so overwhelmed all the time"
                                hide isla
                                
                                narrator "{i}Not doing well is a bit of an understatement. You're being crushed by the burdens of life.{/i}"

                                narrator "{i}She tells you not to stress that much, you only need to pass, you don't have to hold yourself to such a high standard.{/i}"

                                narrator "{i}You know that.{/i}"
                                
                                narrator "{i}But she raised you this way, to always expect nothing but the best from yourself.{/i}"
                                
                                narrator "{i}The contradiction in what you've grown up with and her attitude now, doesn't help with what you're feeling.{/i}"

                                narrator "{i}As she speak, you nod along, mindlessly agreeing with what she's saying.{/i}"

                                narrator "{i}Eventually, the one sided conversation ends and your left to your own devices.{/i}"

                                narrator "{i}It's been such a long time since anyone if your household has been in university, and you're the first person in your 
                                entire family to pursue this kind of degree.{/i}"

                                narrator "{i}It's isolating when the people who are closest to you can't empathize with you.{/i}"

                        "Lie":
                                $ will_to_survive_points -= 5
                                $ relationship_points -= 5

                                show isla anxious at right
                                isla "I'm doing okay, there's just a lot going on right now."
                                hide isla
                                
                                narrator "{i}She looks at you for a second, but she doesn't to press the issue.
                                She leaves you to your noodles, and you're glad that you don't have interact with anyone.{/i}"

                                narrator "{i}You want to tell her how you've been feeling, but you're not really sure yourself.\
                                Nothing horrific has happened, you just feel drained and as though you're not really \"here\"{i}."

                                narrator "{i}You wish you could talk to her about these things, but these conversations have never gone down well in the past.{i}"

                                narrator "{i}She can't comprehend the issues that you're having with your mental health.{i}"
                            
                                narrator "{i}As an immigrant who had to fight to survive in a new country, your problems are not \"real\" problems.{/i}"

                                narrator "{i}All that would have come out of a conversation would have been her telling you to toughen up.{/i}"

                                $renpy.notify("+1 points for saving yourself from a bad conversation")
                                $ will_to_survive_points += 1
                                pause 3
                                
                                scene black with dissolve

                call loading
                jump friendship_with_andrew_and_khashvi

        ##############################################################################################
        #friendship_with_andrew_and_khashvi
        ##############################################################################################
        label friendship_with_andrew_and_khashvi:

                scene courtyard with dissolve 

                narrator "{i}There are some people who do understand your struggle. Maybe not to the same extent, but they are living in the trenches with you.{/i}"

                narrator "{i}You met Khashvi midway through grade 12 when you went to hair school together. 
                That was where you both banded together with another boy named Ethan to survive being with \"blondes\" for nine months.{/i}"

                narrator "{i}She's someone that you trust, respect, and love dearly. Even though she's in a different program, and you don't see her as much as before,\
                you're glad you're doing this together.{/i}"
                
                narrator "{i}You're just two women trying to help each other succeed through this degree.{/i}"

                narrator "{i}On the other hand, you've known Andrew only for a few weeks, but you see and talk to each other nearly every day. It's easy being friends with Andrew.\
                He's open and nonjudgmental, which has made it easy for you to ask him for help in CSC 110.{/i}"
                
                narrator "{i}He's kind and never pokes fun at you for not understanding what's happening in the code.{/i}"
                
                narrator "{i}The two of you often study together, he helps you with computer science, and you constructively rip his English papers to shreds.{/i}"
                
                narrator "{i}(You'd like to think that you're pretty good at writing, despite the allegations that computer scientists can't write.){/i}"
                
                narrator "{i}He's very much a girl's girl and an ally to both you and Khashvi.{/i}"

                call loading
                jump work_life_balance
                
        ###############################################################################################
        #work_life_balance
        ###############################################################################################

        label work_life_balance:
            
                scene bedroom with dissolve 

                narrator "{i}At school, you're starting to find your footing, balancing classes, assignments, friendships, and other commitments.
                There is one thing that has been on your mind: the CSC 110 labs.{/i}" 
                
                narrator "{i}You've mostly been doing them on the weekends because your weeks are so busy. However, that has cut into your time to rest.{/i}"

                menu:
                        "Do you continue to do the labs on the weekends, or do you try to find time during the week?"
                        "Continue to do the labs on the weekends":
                                $ will_to_survive_points -= 5
                                $ academic_points += 5

                                narrator "{i}You continue to do the labs on the weekends, but you're not able to get as much rest as you need.\
                                It takes a few hours out of your time and adds to the list of things to do over the weekend: laundry, meal prep,\
                                washing the dishes, etc.{/i}"

                                narrator "{i}The labs have always been a point of stress for you. They are not worth an insignificant amount of marks,
                                and they help prepare you for the assignments.{/i}"
                                
                                narrator "{i}So despite the extra chunk of time taken away from the weekend, you now go into\
                                labs with more peace of mind. By doing this, you've got into a routine for all your classes.{/i}"

                                call loading
                                jump classes_get_harder 

                        "Try to find time during the week":
                                $ will_to_survive_points -= 5
                                $ academic_points -= 5

                                narrator "{i}You decide to try to find time during the week to do the labs. You're able to find time during the week, but as
                                the weeks go by, you're feeling more and more drained.{/i}"

                                call loading
                                jump classes_get_harder

        ###############################################################################################
        #classes_get_harder
        ###############################################################################################
        # narrator "{i}{/i}"

        label classes_get_harder:

                scene desk with dissolve 

                narrator "{i}With midterms turning their ugly head, life is not getting any easier for anybody. It seems that your professors are trying to make you fail.\
                \"You have two midterms on the same day, too bad\". There's no accommodation in STEM.{/i}"

                narrator "{i}Having assignments, labs, and lectures on top of trying to study for midterms has been overwhelming.\
                You're constantly onto the next thing. Even when you do give yourself a 5 minute break, you feel guilty about taking that time.{/i}"

                call loading

                scene math class with dissolve 

                narrator "{i}Like most Wednesday mornings, you find yourself in math class.{/i}"

                if (met_imen):
                        narrator "{i}You spot Imen sitting with a group of guys.{/i}"

                        menu:
                                "Do you go sit with Imen and those guys at the front or do you find a seat in the middle?"

                                "You find a seat in the middle":

                                        narrator "{i}You find a seat in the middle and get set up for class. While you're waiting for the professor to start the lecture you take\
                                        a look over your assignment.{/i}"

                                        narrator "{i}You would have loved to be able to confirm your results with someone else taking this class. But at this point, you feel like everyone\
                                        has found their group. It would be weird for you to join one now.{/i}"

                                        if (has_tutor):

                                                $ academic_points += 5
                                                $ will_to_survive_points -= 5
                                                $ relationship_points -= 5

                                                narrator "{i}While it would be nice for you to have friends in this class, in the end, all you need to do is pass with a decent mark. i.e. nothing less than 80%%.
                                                You've got a scholarship to keep up!{/i}"

                                                narrator "{i}Besides your sessions with Ryan have been paying off. The marks have been increasing on each assignment.{/i}"
                                            
                                        else:
                                                $ academic_points -= 5
                                                $ will_to_survive_points -= 5
                                                $ relationship_points -= 5

                                                narrator "{i}All the assignments have been going the same way so far...50%%-60%%. It's obvious that you're barely holding on. You can kiss that renewable scholarship goodbye.
                                                You think that in terms of passing the class, you could probably scrape by. But that's something you don't even want to consider right now.{/i}"

                                        call loading
                                        jump office_hours_csc110
                                    
                                "You sit with Imen and those guys":

                                        $ academic_points += 10
                                        $ will_to_survive_points += 10
                                        $ relationship_points += 10

                                        narrator "{i}You take a breath and make your way over to the group, everyone looks at you for a second before Imen speaks up.{/i}"

                                        show imen talking at left
                                        imen "Hi Isla, how's it going?"
                                        hide imen

                                        show isla talking at right
                                        isla "I'm doing as good as I can be. How about you?"
                                        hide isla

                                        show imen talking at left
                                        imen "Not to bad this home work is killer though."
                                        hide imen

                                        show isla talking at right
                                        isla "Tell me about it. I'm almost done, but it's been brutal."
                                        hide isla

                                        show imen talking at left
                                        imen "Me and the guys are almost done too. We're going to work on it today, do you want to join us?"
                                        hide imen

                                        show isla talking at right
                                        isla "For sure!"
                                        hide isla

                                        narrator "{i}After class, you and Imen exchange numbers and agree to meet at the library later tonight.{/i}"

                                        call loading

                                        scene library with dissolve

                                        narrator "{i}Later that night you meet Imen and her friends at the library and have a very productive evening.{/i}"

                                        narrator "{i}You guys meld really well together and were able to finish the questions early on in the evening. 
                                        Without even noticing it, you guys spend a good couple of hours just talking.{/i}"     

                                        narrator "{i}Leaving the library, even though you wasted a bunch of time talking, you feel satisfied with yourself.{/i}"

                                        $renpy.notify("+6 points for getting work done and making friends") 
                                        $ academic_points += 2
                                        $ will_to_survive_points += 2
                                        $ relationship_points += 2
                                        pause 3
                                        
                                        scene black with dissolve

                                        call loading
                                        jump office_hours_csc110      

                else:
                        if (has_tutor):

                                narrator "{i}While it would be nice for you to have friends in this class, in the end, all you need to do is pass with a decent mark. i.e. nothing less\
                                than 80%%. You've got a scholarship to keep up!{/i}"

                                narrator "{i}Besides, your sessions with Ryan have been paying off. The marks have been increasing on each assignment.{/i}"

                                narrator "{i}Since you went to office hours, you've been asking Dr. Bankole questions after class whenever you're unsure of something.{/i}"

                        else:
                                narrator "{i}All the assignments have been going the same way so far... 50%% - 60%%. It's obvious that you're barely holding on.
                                You can kiss that renewable scholarship goodbye. You think that in terms of passing the class, you could probably scrape by.{/i}"

                                narrator "{i}But that's something you don't even want to consider right now.{/i}"

                        narrator "{i}There's a midterm that's coming up. That's been pushed to the back burner in your mind. For now, you're trying to focus on
                        making it one day at a time.{/i}"

                        call loading
                        jump office_hours_csc110

        ###############################################################################################
        #office_hours_csc110
        ###############################################################################################

        label office_hours_csc110:

                scene desk with dissolve 

                narrator "{i}Not only is the Math 122 midterm rearing its head but so is the CSC 110 midterm. You've gotten through the assignments and labs by trial and error.
                So you panicked at first when you heard that it was going to be on paper.{/i}"

                narrator "{i}But after taking a breath, you just committed to kicking it to high gear and locking in on your studies.{/i}"

                narrator "{i}In an effort to get as much practice and master the material, you decide to go over the labs, lectures, quizzes, and assignments.{/i}"

                menu:
                        "Do you go to office hours for help, or do you try to figure it out on your own?"

                        "Figure it out on your own":

                                $ academic_points += 5
                                $ will_to_survive_points += 5

                                narrator "{i}As soon as class ends, you hop on the bus back home. Once you've made it back, you grab a snack and head straight to your bedroom.
                                You lock your door, throw your phone onto the bed, pull out your laptop, and pull up this week's assignment.{/i}"

                                narrator "{i}With another tab open to cover the code body, you go through each method one by one, writing what you think the logic would be on a piece of paper.
                                Once you've finished a question, you uncover it and make corrections.{/i}"

                                narrator "{i}After doing this exercise a couple more times, you begin to get the hang of coding on paper. Moving on, you go back to the previous quizzes.
                                These are harder to answer, not because they're difficult but because you can remember what you put down previously.{/i}"

                                show isla talking at right
                                isla "Maybe I can do this...it's not as bad as I thought it was going to be."
                                hide isla 

                                narrator "With the momentum, you continue to study late into the night."

                                call loading
                                jump write_math122_midterm

                        "Go to office hours":

                                $ academic_points += 5
                                $ will_to_survive_points += 5
                                $ relationship_points += 5
                                
                                scene lecture hall with dissolve 

                                narrator "{i}After class is over, you meet with Khashvi and head over to one of the big lecture halls.
                                The Women in Engineering and Computer Science Club (WECS) is hosting a review session for CSC 110.{/i}"

                                $renpy.notify("+1 points for trying")
                                pause 3
                                $ will_to_survive_points -= 1

                                narrator "{i}Maybe it's because it's so late in the evening, but it's only you, Khashvi, two TAs, and Dr. Hones in the room. It's almost silent.
                                As quietly as possible, the two of you sit down.{/i}"

                                narrator "{i}Khashvi works on her homework while you're trying to go through this week's assignment. You're so stumped on a problem that you haven't
                                noticed that Dr. Hones has walked up to you and is looking over your shoulder.{/i}"

                                show emma talking at left 
                                emma "Hey, how's it going?"
                                hide emma

                                show isla surprised at right 
                                isla "It's going okay, I'm just stuck on this question."
                                hide isla 

                                show emma talking at left
                                emma "What are you stuck on?"
                                hide emma

                                narrator "{i}You show her the question.{/i}"

                                show emma talking at left
                                emma "{i}Where do you think you should start?{/i}"
                                hide emma 

                                narrator "{i}Honestly, you don't even know where to start. That's why you've been looking at it for the past ten minutes.{/i}"

                                menu:
                                        "Do you tell Dr. Hones that you don't know where to start? Or do you come up with something that's probably wrong?"

                                        "Tell Dr. Hones that you don't know where to start":

                                                $ academic_points -= 5
                                                $ will_to_survive_points -= 5
                                                $ relationship_points += 5

                                                narrator "{i}You were not expecting her to come up to you and ask you if you needed help so directly. With the room being almost silent, it feels
                                                like you've just been called out. The thoughts that you're currently having are completely irrational.{/i}"

                                                narrator "{i}It feels like by admitting to not knowing, you're admitting that you don't belong with the rest of the intellectuals here.{/i}"

                                                narrator "{i}By saying \"I need help\" on what should be a simple question, feels like saying \"I don't belong in comp sci\".{/i}"

                                                narrator "{i}In an anxious rush you blurt out,{/i}"

                                                show isla indifferent at right
                                                isla "I don't know where to start."
                                                hide isla

                                                narrator "{i}Dr. Hones nods and takes a look at the question.{/i}"

                                                narrator "{i}She starts to explain what we need to accomplish in this question, but you can't follow. Your mind is spiralling.{/i}"

                                                show emma talking at left
                                                emma "{i}We need to create a list of all the student SIDs. How can we go about doing that?{/i}"
                                                hide emma

                                                narrator "{i}She looks at you expectantly. You probably know this, but your anxiety has taken off, and your head is empty.
                                                All you can think about is messing up in front of her.{/i}"

                                                narrator "{i}Time is ticking.{/i}"
                                                
                                                narrator "{i}All you can do is stare at the screen.{/i}"

                                                narrator "{i}You must have taken too long because Dr. Hones chimes in.{/i}"

                                                show emma talking at left
                                                emma "{i}How can you go through a list of students?{/i}"
                                                hide emma 

                                                narrator "{i}You blurt something out...It must have been so wrong because she looks at you blankly before proceeding to explain the logic.{/i}"

                                                narrator "{i}You can't even listen to what she's saying because it feels like everything that you thought about earlier is true.{/i}"
                                                
                                                narrator "{i}Thinking about the guys in your class who've been doing this since high school, you have no idea how you're going to catch up. You don't belong with these people.{/i}"
                                            
                                        "Come up with something that's probably wrong":

                                                $ academic_points -= 5
                                                $ will_to_survive_points -= 5
                                                $ relationship_points += 5

                                                narrator "{i}You don't know what possesses you. In your mind, you know it's not right, but your words come out with full confidence and strength.{/i}"

                                                show isla talking at right
                                                isla "An if statement"
                                                hide isla 
                                                
                                                narrator "{i}For a second she gives you a blank look.{/i}"

                                                show emma confused at left
                                                emma "Good try..."
                                                hide emma 

                                                narrator "{i}She then proceeds to explain the logic behind the question.{/i}"

                                                narrator "{i}You can't even listen to what she's saying because you feel like an idiotic fraud. Thinking about the guys in your class who've 
                                                been doing this since high school, you have no idea how you're going to catch up. You don't belong with these people.{/i}"

                                narrator "{i}After she finishes explaining the question, you thank her and lean over to Khashvi and whisper,{/i}"

                                show isla indifferent at right
                                isla "I've finished asking all my questions. Let's go?"
                                hide isla 

                                show khashvi talking at left
                                khashvi "Sure, let's go."
                                hide khashvi

                                scene bus stop with dissolve

                                narrator "{i}You and Khashvi leave the room and head to the bus stop.{/i}"

                                narrator "{i}What happened during office hours was mortifying. Aside from the embarrassment, this experience has you really doubting yourself.
                                Not just for the midterm, but for the future.{/i}"
                                
                                narrator "{i}If you're just scraping by computer science classes now, with the support of your friends and 
                                people like the WECS, how are you going to stand in a field dominated by men?{/i}"

                                $ went_to_office_hours = True

                                call loading
                                jump write_math122_midterm

        ##############################################################################################
        #write_math122_midterm
        ##############################################################################################

        label write_math122_midterm:

                scene math class with dissolve

                narrator "{i}Soon enough, the Math 122 midterm rolls around, hardly any time after is the CSC 110 midterm.{/i}"

                narrator "{i}The classroom is packed like sardines. On regular days, 60%% of the class doesn't show up, so to see everyone here is a lot.
                Like the last midterm, everyone is radiating nervous energy.{/i}"

                narrator "{i}You take a seat at one of the chairs. This classroom sucks for midterms. Not just because it is small, but because
                the chairs have arm desks. There's hardly any space for your paper, let alone any stationary.{/i}"

                narrator "{i}A TA distributes the tests face down. As they come around, you sit cramped between two other students with your pencils and eraser in
                your lap.{/i}"

                narrator "{i}Once all the papers have been distributed, Dr. Bankole says some words.{/i}"

                show drBankole talking at left
                drBankole "{i}You have 50 minutes for the midterm. The TAs will write the time down on the board every 10 minutes.
                If you get stuck on a question, move on to the next. Ration your time wisely.{/i}"
                hide drBankole

                narrator "{i}Dr. Bankole looks at the time and announces,{/i}"

                show drBankole talking at left
                drBankole "You may begin."
                hide drBankole

                narrator "{i}As soon as she says that, there is a great rustle of paper.{/i}"

                scene midterm paper with dissolve

                narrator "{i}You take a deep breath and open your test. You flip through each of the pages.{/i}"

                if met_imen and has_tutor:
                        narrator "{i}Skimming through the pages, everything looks familiar to you. You've done similar questions before in your practice.{/i}"

                        narrator "{i}Doing late nights with Imen and meeting with Ryan has really helped you get familiar with the topics.{/i}"
                
                elif met_imen and not has_tutor:
                        narrator "{i}Skimming through the pages, everything looks familiar to you. You've done most of these questions correctly in your practice.{/i}"

                        narrator "{i}Meeting Imen and forming a study group with her has really helped you get familiar with the topics.{/i}"
                    
                elif not met_imen and has_tutor:
                        narrator "{i}Skimming through the pages, everything looks familiar to you. You've done most of these questions correctly in your practice.{/i}"

                        narrator "{i}Doing the weekly sessions with Ryan has really helped you get familiar with the topics.{/i}"

                else:
                        narrator "{i}Skimming through the pages, you've seen everything before. But you're at a loss at how to answer the questions.{/i}"

                narrator "{i}You take breath, put your head down, and begin answering questions.{/i}"

                call loading

                scene midterm paper with dissolve

                narrator "{i}Time is ticking, and you're furiously trying to write and come up with something for this final proof question.{/i}"

                narrator "{i}Viciously, your scribbling down words. The text is getting larger and messier by the second.{/i}"

                narrator "{i}Think, think, think.{/i}"
                
                narrator "{i}How do you prove the opposite direction of this if and only if proof?{/i}"

                scene math class with dissolve

                show drBankole talking at left
                drBankole "5 minutes left."
                hide drBankole

                scene midterm paper with dissolve

                narrator "{i}You're stressed, you haven't finished this question, and you have yet to look over your test.{/i}"

                narrator "{i}Screw it you think. You drop this last question and go back to the first.{/i}"

                narrator "{i}With the last 5 minutes, you quickly glance over the rest of your test for glaring mistakes.{/i}"

                scene math class with dissolve

                show drBankole talking at left
                drBankole "Time's up. Stop writing or else it's a 0!"
                hide drBankole

                narrator "{i}You put your pencil down and sit back in your chair. You're exhausted.{/i}"

                narrator "{i}Slowly you pick up your things and begin to pack up. You can hear others talking about the test,
                but you ignore it. If anything, hearing them say something contradictory to what you did is only going to make you feel worse.{/i}"

                scene hallway with dissolve

                if met_imen:
                        narrator "{i}Stepping out of the class, you see Imen waiting for you.{/i}"

                        show imen talking at left
                        imen "How did you find the test?"
                        hide imen

                        show isla talking at right
                        isla "It was okay, I think I did enough to pass. What about you?"
                        hide isla

                        show imen talking at left
                        imen "I think I did okay too. Do you have anymore midterms?"
                        hide imen

                        show isla talking at right
                        isla "Yeah, I have one for CSC 110."
                        hide isla

                        show imen talking at left
                        imen "Good luck with that! I'm sure you'll do great!"
                        hide imen

                        scene bus stop with dissolve

                        narrator "{i}You and Imen part ways and you head home.{/i}"

                        narrator "{i}As the saying goes, there is no rest for the wicked. Once you get back home, you're back on the CSC 110 grind.{/i}"

                else:
                        narrator "{i}Stepping out of the class you feel drained. All you can do is hope that what you put out there was enough.{/i}"

                        narrator "{i}Even though your exhausted, you still have CSC 110 to study for. There is no rest for the wicked. Once you get back home, 
                        you're back on the CSC 110 grind.{/i}"

                call loading
                jump write_csc110_midterm

        ##############################################################################################
        #write_csc110_midterm
        ##############################################################################################

        label write_csc110_midterm:

                scene night with dissolve 
                
                narrator "{i}It's the day of the midterm, and you and Andrew have agreed to meet in the library before going to the midterm.
                You think that the midterm being outside of class time is absurd.{/i}"
                
                narrator "{i}Having to come back to campus for the 7:00 PM midterm is exhausting. Especially since you had class earlier this morning.{/i}"

                narrator "{i}While you were at home, you did some last minute review. During that time, you realized that you completely don't understand
                loops, neither for, while, or nested loops.{/i}"

                if (went_to_office_hours):
                        narrator "{i}This was what Dr. Hones was trying to explain during office hours, but you were too panicked to absorb anything.{/i}"
                
                menu:
                        "You know you're going to see Andrew before the midterm, do you ask him for help or not?"

                        "Ask him for help":
                                $ academic_points -= 5
                                $ will_to_survive_points += 5
                                $ relationship_points += 5
                                
                                narrator "{i}As soon as you see him in the library, you pull out your ipad and show him one of the pre-lecture quizzes.{/i}"

                                show isla indifferent at right
                                isla "I don't understand loops."
                                hide isla 

                                show andrew neutral at left
                                andrew "What do you mean? Didn't you do the assignment?"
                                hide andrew

                                show isla indifferent at right
                                isla "I somehow did the assignment without understanding them."
                                hide isla 

                                show andrew neutral at left
                                andrew "Okay, let's go over this."
                                hide andrew

                                narrator "{i}Andrew the proceeds to give you a crash course on for, while, and nested loops in 15 minutes. You just hope that whatever he said sticks.{/i}"
                            
                        "Don't ask him for help":

                                $ academic_points -= 5
                                $ will_to_survive_points -= 5
                                $ relationship_points -= 5

                                narrator "{i}You decide to just go with what you know. By the time you make it to the library, there's not going to be enough time to actually
                                learn anything.{/i}"

                                scene library with dissolve

                                narrator "{i}With extra time before the midterm, you meet up with Andrew at the library, and the two of you 
                                chill for a bit before heading out.{/i}"
                    
                scene night time school yard with dissolve

                narrator "{i}The two of you head over to the ECS Building. The hallway outside the lecture hall is filled with stressed-out students.
                It's claustrophobic and hot, and the air is buzzing. You can feel everyone else's tension.{/i}"

                scene lecture hall with dissolve 

                narrator "{i}Soon, 200 students are let into the lecture hall, and you and Andrew sit down to write the test.{/i}"

                narrator "{i}Once everyone is situated, Dr. Hones begins speaking.{/i}"

                show emma talking at left

                emma "Some notes before you get started. This is a 50-minute midterm, and there are six questions to answer.
                Since there are so many of you, we will not be answering questions."
                
                emma "If you have a question, write down your assumption. If it is reasonable, we will take it into consideration when marking your test."

                emma "For a lot of you, this might be the first midterm you've ever taken in university. So, I understand that there may be a lot of nerves tonight. 
                But you guys have studied hard for this. I am sure everything is going to be okay."

                hide emma

                narrator "{i}There are two minutes left on the clock.{/i}"

                show emma talking at left
                emma "You may begin as soon as the clock hits 7:00 PM. Good luck everyone!"
                hide emma

                narrator "{i}As soon as the clock hits 7, there is a great rustle of paper.{/i}"

                narrator "{i}As soon as you open the test's cover, everything that you studied leaves your brain. There's so much documentation, and even though you practiced writing code, 
                the format is completely unfamiliar.{/i}"

                scene midterm paper with dissolve 

                narrator "{i}First page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Second page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Third page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Fourth page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Fifth page, you can't answer anything... flip the page.{/i}"
                
                narrator "{i}Sixth page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Seventh page, you can't answer anything... flip the page.{/i}"

                narrator "{i}Eighth page, you can't answer anything... flip the page.{/i}"

                scene black with dissolve
                narrator "{i}You've made it to the end of the test...{/i}"

                call loading 

                jump s1t1_ending

        # narrator "{i}{/i}"
        ##############################################################################################
        #s1t1_ending
        ##############################################################################################
        # narrator "{i}{/i}"

        label s1t1_ending:

                scene school night with dissolve 

                narrator "{i}You've got through the first set of midterms for this semester.{/i}"

                narrator "{i}You're absolutely exhausted.{/i}"

                narrator "{i}You want to sleep and never wake up again.{/i}"

                narrator "{i}The hour is late, it's dark, and it's starting to rain hard outside.{/i}"
                
                narrator "{i}You're in the ECS building working through your other assignments when suddenly
                you get two consecutive notifications on your laptop.{/i}"

                scene laptop with dissolve

                narrator "{i}CSC110 Notification: Grades released for midterm 1...{/i}"

                narrator "{i}MATH122 Notification: Grades for midterm 1...{/i}"

                narrator "{i}Your heart is pounding, you're not sure if you want to look at the grades or not.{/i}"

                narrator "{i}Deciding not to push the inevitable, you go to the course page and look at the grades.{/i}"

                narrator "{i}You look at the Math 122 marks first.{/i}"

                if met_imen and has_tutor:

                        $ academic_points -=  15
                        $ will_to_survive_points -= 10

                        narrator "{i}You got a 60%% on the midterm. It's not the best, and you're not happy with yourself for it, but a pass is a pass.
                        An engineering and computer science pass nonetheless.{/i}"

                        narrator "{i}With all the work that you did, and the help that you got, was this really the best you could do?{/i}"

                        narrator "{i}With a sad sigh you accept your results. It is what it is. You're just going to have to make it up in the 
                        next midterm.{/i}"

                elif (met_imen and not has_tutor) or (not met_imen and has_tutor):

                        $ academic_points -= 20
                        $ will_to_survive_points -= 15

                        narrator "{i}You got a 50%% on the midterm. It's not the best, you expected better. It's not even enough to be considered an
                        engineering and computer science pass.{/i}"

                        narrator "{i}With all the work that you did and the help that you got, was this really the best you could do?{/i}"

                        narrator "{i}With a sad sigh, you accept your result. It is what it is. You're just going to have to make it up in the 
                        next midterm.{/i}"

                else:

                        $ academic_points -= 25
                        $ will_to_survive_points -= 20

                        narrator "{i}You got a 45%% on the midterm.{/i}"

                        narrator "{i}You feel like you should cry and be upset, but all you feel is numbness. All those negative thoughts that you
                        have had all semester seem to be true.{/i}"

                narrator "{i}With a heavy heart, you change tabs and look at the CSC 110 marks next.{/i}"

                $ academic_points -= 15
                $ will_to_survive_points -= 10

                narrator "{i}60%%.{/i}"

                if (academic_points >= 60 and will_to_survive_points >= 60 and relationship_points >= 50):

                        narrator "{i}Coming out of that midterm you didn't think you were going to pass that one.
                        For sure it's not great, but you're just glad that you managed to passed.{/i}"

                        call loading 

                        scene black with dissolve

                        narrator "{i}Congratulations! You have lived to survive another day.{/i}"

                        narrator "{i}Let's see, do you have the will to complete another semester?{/i}"

                        show text "TO BE CONTINUED..." with Pause(5, Hard=True)

                else:
                        scene black with dissolve

                        narrator "{i}You're not sure what to do.{/i}"

                        narrator "{i}You're not sure if you can do this.{/i}"

                        narrator "{i}You're not sure if you want to do this.{/i}"

                        narrator "{i}No, you don't want to do this anymore...{/i}"

                        show text "GAME OVER" with Pause(5, Hard=True)

        ##############################################################################################
        #loading
        ##############################################################################################

        label loading:
                scene black
                show text "Loading..." with Pause(3, Hard=True)
                return

return