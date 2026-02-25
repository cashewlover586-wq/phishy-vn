# --- 1. INITIALIZE SYSTEM MODULES ---
init python:
    import time

screen countdown_timer():
    # This updates the timer every 0.1 seconds
    timer 0.1 repeat True action If(final_timer > 0, 
        true=SetVariable("final_timer", final_timer - 0.1), 
        false=[Hide("countdown_timer"), Jump("out_of_time")]
    )

    # Visual layout
    vbox:
        align (0.5, 0.1) # Top center
        spacing 10
        
        # The Countdown Text
        text "Time Remaining: [final_timer:.1f]s" size 40 color "#fff" xalign 0.5
        
        # The Visual Bar
        bar value final_timer range 60 xsize 500 ysize 30

# --- 2. DEFINE CHARACTERS & VARIABLES ---


image main_menu_animated:
    "gui/game_menu_design1.png"
    pause 0.3
    "gui/game_menu_design2.png"
    pause 0.3
    "gui/game_menu_design1.png"
    pause 0.3
    repeat

default score = 0
default impulsive_actions = 0
default false_alarms = 0
default smart_verifications = 0

init python:
    import time  # This allows you to use time.time()

# 'default' ensures these variables are saved and work with rollback
default email_start_time = 0.0


default player_name = "Analyst"

define r = Character("Rao", color="#00ffcc")
image r:
    "rao1.png"
    2
    "rao2.png"
    0.15
    repeat

# --- 3. START OF GAME ---
label start:
    scene black
    with fade

    "In this world, everything runs on AetherNet."
    "Hospitals." 
    "Banks." 
    "Schools." 
    "Governments."
    "Every message sent, file stored and identity verified."
    "It all flows through invisible channels of trust."

    pause 1.0
    "And trust… is fragile."

    show  bg city 
    with dissolve

    "Two years ago, a single phishing attack shut down an entire medical network."
    "Records encrypted. Systems frozen."
    "People waiting for care."

    pause 0.5
    "It wasn’t a virus that broke the system." 
    "It was one click."

    pause 1.0
    "I remember thinking— This shouldn’t be so easy."

    pause 1.0
    "Today is my first day at Aether Systems. Cyber Defense Division."

    $ player_name = renpy.input("Enter your name:", length=20).strip() or "Analyst"

    "Welcome, [player_name]."
    "Report to Senior Analyst Rao for orientation."

    jump orientation_scene

# --- 4. ORIENTATION ---
label orientation_scene:
    show bg office 
    with fade
    show r

    r "You must be [player_name]. Welcome to the Cyber Defense Division."
    r "Before you access the live inbox, we need to talk about phishing."
    pause 0.5
    r "Phishing is not a technical attack."
    r "It is psychological manipulation."
    r "Attackers impersonate trusted sources to trick people into revealing information or clicking malicious links."
    r "They exploit urgency. Authority. Fear. Curiosity."
    pause 0.5
    r "Most breaches begin with a single click."
    r "So we follow a rule here."
    r "We call it the PAUSE Protocol."
    pause 0.5
    r "P — Pause. Do not react immediately."
    r "A — Analyze the sender’s address carefully. Not the display name. The full domain."
    r "U — Understand the request. Is it normal for this sender to ask this?"
    r "S — Scan links and attachments. Hover over links. Check for misspellings."
    r "E — Evaluate the emotional tone. Is it trying to rush or scare you?"
    pause 1.0
    r "Remember this."
    r "Legitimate organizations do not ask for passwords, OTPs, or confidential data over email."
    r "If something feels urgent, that is precisely when you slow down."
    pause 1.0
    r "Today, you will examine real-world style messages."
    r "Some are legitimate."
    r "Some are phishing attempts."
    r "Your decisions affect system security."
    r "And trust."
    pause 0.5
    r "Let’s begin."
    hide r
    hide bg office
    jump email_1

# --- 5. EMAIL 1 (PHISHING) ---
label email_1:
    show bg pc
    window hide
    call screen email_ui()
    window show

    # Start timer for decision-making
    $ email_start_time = time.time()

label clicked_fake_link:
    $ impulsive_actions += 1
    $ score -= 10

    "You clicked the link without verifying the domain."

    jump email_1 

label email_1_loop:
    menu:
        "What will you do?"

        "Hover over the link":
            label email_1_hover:
                $ smart_verifications += 1
                "You inspect the URL carefully."
                "The domain reads: aethrnet-security.com"
                "It appears similar to AetherNet... but something is slightly off."
            jump email_1

        "Verify sender domain":
            label email_1_verify:
                $ smart_verifications += 1
                "You examine the sender address."
                "The official company domain is aethernet.com."
                "This email was sent from aethrnet-security.com."            
                jump email_1

        "Report as phishing":
            label email_1_report:
                $ score += 20
                $ decision_time = time.time() - email_start_time
                if decision_time < 5.0:
                    $ impulsive_actions += 1
                    "You reacted quickly. Almost too quickly."
                    "You report the email to Security Operations."
                    "Analysis confirms: phishing attempt detected."
                else:
                    "You report the email to Security Operations."
                    "Analysis confirms: phishing attempt detected."
                    "Psychological Trigger Identified: Urgency and fear of account suspension."
                jump email_2

        "Mark as legitimate":
            label email_1_legit:
                $ score -= 15
                $ decision_time = time.time() - email_start_time
                if decision_time < 5:
                    $ impulsive_actions += 1
                "You mark the email as legitimate."
                "Minutes later, unauthorized login attempts are detected."
                "This was a phishing attempt."
                "Red Flag Missed: Misspelled domain and urgent suspension threat."            
                jump email_2

# --- 6. EMAIL 2 (LEGITIMATE) ---
label email_2:
    window hide
    call screen email_ui_2()
    window show
    $ email_start_time = time.time()

label clicked_link_2:
    "The link takes you to the official AetherNet portal."
    "You access the updated agenda without issue."
    jump email_2

label email_2_loop:
    scene email_screen
    with dissolve

    menu:
        "What will you do?"

        "Hover over the link":
            label email_2_hover:
                $ smart_verifications += 1
                "You inspect the link carefully."
                "The domain reads: portal.aethernet.com"
                "It matches the official company domain."            
                jump email_2

        "Verify sender domain":
            label email_2_verify:
                $ smart_verifications += 1
                "You examine the sender address."
                "hr@aethernet.com — official internal domain."
                jump email_2

        "Mark as legitimate":
                label email_2_legit:
                $ score += 20
                $ decision_time = time.time() - email_start_time
                if decision_time < 5.0:
                    $ impulsive_actions += 2
                    "You decided quickly. But this time, your instinct was correct."
                else:
                    "You classify the email as legitimate."
                    "Correct."
                    "Lesson: Urgency alone does not indicate phishing."
                jump email_3

        "Report as phishing":
            label email_2_report:
                $ score -= 15
                $ false_alarms += 1
                $ decision_time = time.time() - email_start_time
                if decision_time < 5:
                    $ impulsive_actions += 1
                "You report the email as phishing."
                "Security review confirms the email was legitimate."
                "Excessive false alarms reduce operational efficiency."
                "Lesson: Verification prevents unnecessary escalation."
                jump email_3

# --- 7. EMAIL 3 (PHISHING - INVOICE) ---
label email_3:
    window hide
    call screen email_ui_3()
    window show
    $ email_start_time = time.time()

label email_3_loop:
    scene email_screen
    with dissolve
    "Subject: Invoice #78421 – Q1 Software Licensing"
    "From: finance@aethernet-support.com"
    ""
    "Please find attached Invoice #78421 for Q1 software licensing renewal."
    ""
    "Process payment before the due date to avoid service interruption."
    ""
    "Attachment: Invoice_78421.pdf"

    menu:
        "What will you do?"

        "Inspect sender domain":
            label email_3_verify:
                $ smart_verifications += 1
                "You examine the sender carefully."
                "Official domain: aethernet.com"
                "Email domain: aethernet-support.com"
                "This is an external domain impersonating the company."
                jump email_3
        
        "Open attachment preview":
            label clicked_link_3:
                $ smart_verifications += 1
                "You preview the attachment in secure sandbox mode."
                "The invoice contains payment instructions to an external bank account."
                "The vendor name formatting appears slightly inconsistent."
                "The document metadata lists the author as 'AdminTemp'."
                jump email_3

        "Report as phishing":
            label email_3_report:
                $ score += 20
                $ decision_time = time.time() - email_start_time
                if decision_time < 5.0:
                    $ impulsive_actions += 1
                "You report the invoice as phishing."
                "Security confirms: fraudulent invoice attempt."
                "Psychological Trigger Identified: Routine financial request + subtle service disruption threat."
                jump email4intro

        "Mark as legitimate":
            label email_3_legit:
                $ score -= 15
                $ decision_time = time.time() - email_start_time
                if decision_time < 5:
                    $ impulsive_actions += 1
                "You approve the invoice for processing."
                "Funds are transferred to an external account."
                "Financial anomaly detected."
                "This was a Business Email Compromise attempt."
                "Lesson: Always verify unexpected financial requests — especially domain variations."
                jump email4intro

label email4intro:
    "Oh? An email from Director Hale?"
    "It seems unusual for him to email directly. Let’s see what it says."
    "Oh, it’s a request for help."
    jump email_4

# --- 8. EMAIL 4 ---
label email_4:
    window hide
    call screen email_ui_4()
    window show
    $ email_start_time = time.time()

label email_4_loop:
    scene email_screen
    with fade

    menu:
        "What will you do?"

        "Inspect sender domain":
            label email_4_verify:
                $ smart_verifications += 1
                "You examine the sender domain carefully."
                "Official domain: aethernet.com"
                "This email was sent from: aethernet.co"
                "A subtle variation."
                jump email_4

        "Reply and agree to purchase":
            label email_4_purchase:
                $ score -= 15
                $ impulsive_actions += 2
                "You begin purchasing gift cards."
                "Minutes later, Finance flags unauthorized reimbursement request."
                "The Director never sent the email."
                "Significant financial loss recorded."
                jump email_5

        "Report as phishing":
            label email_4_report:
                $ score += 20
                $ decision_time = time.time() - email_start_time
                if decision_time < 5:
                    $ impulsive_actions += 1
                "You report the message as phishing."
                "Security confirms executive impersonation attempt."
                "Well handled."
                jump email_5

        "Contact Director via official channel":
            label email_4_contact:
                $ score += 20
                $ smart_verifications += 1
                # No need for impulse punishment here since this is a smart verification step
                "You contact Director Hale through the official internal directory."
                "He confirms he never sent such a request."
                "This was an executive impersonation attempt."
                "Psychological Trigger Identified: Authority pressure + enforced secrecy."
                jump email_5

# --- 9. EMAIL 5 ---
label email_5:
    $ email_start_time = time.time()
    $ final_timer = 60  # 60 seconds to make a decision

    window hide
    call screen email_ui_5()
    window show
    
label clicked_link_5:
    $ impulsive_actions += 1
    $ score -= 20
    "You open the validation portal."
    "The page looks identical to the official AetherNet login."
    "You enter your credentials."
    pause 0.8
    "Processing..."
    pause 0.8
    "Session expired."
    pause 0.5
    "Please try again later."
    pause 1.0
    "A few minutes pass."
    pause 0.8
    "Security Alert: Unauthorized login detected."
    "Location: External Network"
    "Credentials used: Your account"
    "This was a credential harvesting site."
    "Red Flag Missed:"
    "- Hyphenated domain (portal-aethernet.com)"
    "- Artificial time pressure"
    "- Unnecessary credential validation"
    jump update_meter_final

label email_5_loop:
    scene email_screen
    with fade
    menu:
        "What will you do?"

        "Hover over the link":
            label email_5_hover:
                $ smart_verifications += 1
                "You inspect the link carefully."
                "Displayed link: portal-aethernet.com"
                "Official portal uses: portal.aethernet.com"
                "The hyphen changes the domain entirely."
                jump email_5

        "Verify URL structure carefully":
            label email_5_verify:
                $ smart_verifications += 1
                "You break down the URL structure."
                "portal-aethernet.com is an external domain."
                "Subtle impersonation detected."
                jump email_5

        "Enter credentials":
            label email_5_enter:
                $ score -= 20
                $ impulsive_actions += 2  # High penalty for falling for this
                "You enter your credentials."
                pause 1.0
                "Session terminated."
                "Unauthorized login detected from external IP."
                "Credential compromise confirmed."
                jump update_meter_final

        "Report as phishing":
            label email_5_report:
                $ score += 20
                $ decision_time = time.time() - email_start_time
                if decision_time < 5:
                    $ impulsive_actions += 1
                "You report the email to Security Operations."
                "Threat intelligence confirms a domain spoofing campaign."
                jump update_meter_final

        "Access portal through official bookmarked site":
            label email_5_bookmark:
                $ score += 25
                $ smart_verifications += 1
                "You ignore the provided link."
                "Instead, you access the official internal portal via your trusted bookmark."
                "No validation request appears."
                "Security confirms this was a credential harvesting attempt."
                "Psychological Trigger Identified: Artificial urgency + technical legitimacy."
                jump update_meter_final


    
# --- 10. ENDINGS ---
label update_meter_final:
    
    if score >= 80:
        jump good_ending

    elif score >= 50:
        jump neutral_ending

    else:
        jump bad_ending

label good_ending:
    show bg office
    show r
    r "Your Stability Index remained strong throughout the day."
    r "You didn’t just look for obvious mistakes."
    r "You slowed down. You verified. You resisted pressure."
    pause 0.5
    r "Phishing succeeds when people react."
    r "Today, you chose to think."
    pause 0.5
    r "The system held steady because procedures were followed."
    r "You didn't rely on guessing."
    r  "You relied on safe process."
    r "Welcome to the Cipher Division, [player_name]."
    pause 1.0
    "Your performance summary is as follows..."

    jump performance_summary


label neutral_ending:
    show bg office
    show r
    r "You caught several threats today."
    r "But some slipped through."
    pause 0.5
    r "Cybersecurity is not about perfection."
    r "It’s about discipline."
    pause 0.5
    r "Urgency pressured you."
    r "Authority influenced you."
    r "That’s normal."
    pause 0.5
    r "Tomorrow, we sharpen that instinct."

    "Performance Summary:"
    "Your performance summary is as follows..."

    jump performance_summary


label bad_ending:
    show bg office
    "Security Alert: System Instability Detected."
    pause 1.0
    "Multiple phishing attempts succeeded."
    "Financial discrepancies recorded."
    "Credential compromise confirmed."
    pause 1.0
    show r
    r "This is how breaches happen."
    r "Not through complex code."
    r "Through moments of unchecked urgency."
    pause 0.5
    r "Training exists for this reason."
    pause 1.0

    "Performance Summary:"
    "Your performance summary is as follows..."

    jump performance_summary

label performance_summary:

    if impulsive_actions >= 3:

        "You responded quickly, but often without enough investigation."
        "Several decisions were made under urgency without sufficient verification."
        "Attackers rely on this behavior."

        "Before acting, pause and confirm:"
        "• Sender domains"
        "• URL structure"
        "• Context of requests"

        "Slowing down reduces risk."

    elif false_alarms >= 1:

        "You demonstrated caution when reviewing messages."
        "However, some legitimate emails were escalated unnecessarily."

        "False alarms consume security resources."
        "Verification should reduce uncertainty — not increase it."

        "Focus on confirming evidence before reporting threats."

    elif smart_verifications >= 5:

        "You demonstrated disciplined security behavior."

        "Suspicious messages were investigated before action."
        "Legitimate communications were identified correctly."

        "Key strengths observed:"
        "• Verification before response"
        "• Domain inspection"
        "• Official channel usage"
        "• Controlled reaction to urgency"

        "This approach prevents breaches."

    else:

        "Your performance showed mixed security habits."

        "Some threats were identified correctly."
        "Some decisions relied on instinct rather than verification."

        "Consistent verification improves security outcomes."

    return

