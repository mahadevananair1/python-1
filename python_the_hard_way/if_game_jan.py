print("""You enter Jan Poonthong park game, this game is base on luck
Which door do you want to go through #1 or #2?""")

door = input(">>> ")

# Elon Musk
if door == "1":
    print("There's Elon Musk waiting to talk with you!")
    print("What do you do?")
    print("1. Ask Elon for some money.")
    print("2. Take valuable advice from Elon.")

    elon = input(">>> ")

    if elon == "1":
        print("Elon never give out money to people with no purpose")
        print("You made wrong decision with a billionaire")
        print("Next time think before you make a decision")
    elif elon == "2":
        print("Elon is always willing to help young generation")
        print("Press RETURN to get Elon advice to you Or CTRL-C to not take advice.")

        input(">>> ")

        print("Work every waking hours, put 90 - 100 hours of work every week, the odds of suceeseding is more")
    else:
        print("Elon don't know want you want!")

# Eminem
elif door == "2":
    print("There's Eminem waiting to talk with you!")
    print("What do you do?")
    print("1. Rap battle with Eminem.")
    print("2. Take valuable advice from Eminem.")

    eminem = input(">>> ")

    if eminem == "1":
        print("You are in battle with Eminem now.")
        print("Write down your rap here.")
        user_rap = input(">>> ")
        print("Now is Eminem turn.")
        print("Press RETURN to see Eminem rap to you Or CTRL-C to not.")

        input(">>> ")

        print("""                You sound like a bitch, bitch
                Shut the fuck up
                When your fans become your haters
                You done?
                Fuckin' beard's weird
                Alright
                You yellin' at the mic, fuckin' weird beard (You want smoke)
                We doin' this once
                You yellin' at the mic, your beard's weird
                Why you yell at the mic? (Illa)

                Rihanna just hit me on a text
                Last night I left hickeys on her neck
                Wait, you just dissed me? I'm perplexed
                Insult me in a line, compliment me on the next
                Damn, I'm really sorry you want me to have a heart attack
                Was watchin' 8 Mile on my NordicTrack
                Realized I forgot to call you back
                Here's that autograph for your daughter, I wrote it on a Starter cap
                Stan, Stan, son
                Listen, man, Dad isn't mad
                But how you gonna name yourself after a damn gun
                And have a man-bun?
                The giant's woke, eyes open, undeniable
                Supplyin' smoke, got the fire stoked
                Say you got me in a scope, but you grazed me
                I say one call to Interscope and you're Swayze
                Your reply got the crowd yelling, "Woo!"
                So before you die let's see who can out-petty who
                With your corny lines ("Slim, you're old")—ow, Kelly, ooh
                But I'm 45 and I'm still outselling you
                By 29, I had three albums that had blew
                Now let's talk about somethin' I don't really do
                Go in someone's daughter's mouth stealin' food
                But you're a fuckin' mole hill
                Now I'ma make a mountain out of you, woo!""")

    elif eminem == "2":
        print("Eminem is always willing to help young generation")
        print("Press RETURN to get Elon advice to you Or CTRL-C to not take advice.")

        input(">>> ")

        print("Practice, Perform, Network and Share! - Eminem")

else:
    print("You didn't choose anything, you're out of game.")
