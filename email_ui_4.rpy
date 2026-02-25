screen email_ui_4():

    modal True

    hbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        # LEFT SIDE - ACTION PANEL
        frame:
            xsize 250
            ysize 600
            padding (20,20)
            background "#e8e8e8"

            vbox:
                spacing 20

                text "Actions" size 28 color "#000000"

                textbutton "Inspect Sender Domain":
                    text_size 24
                    action [Return(), Jump("email_4_verify")]

                textbutton "Reply and agree to purchase":
                    text_size 24
                    action [Return(), Jump("email_4_purchase")]

                textbutton "Report Phishing":
                    text_size 24
                    action [Return(), Jump("email_4_report")]

                textbutton "Contact Director Hale via official channel":
                    text_size 24
                    action [Return(), Jump("email_4_contact")]


        # RIGHT SIDE - EMAIL CONTENT
        frame:
            xsize 900
            ysize 600
            padding (40,40)
            background "#ffffff"

            vbox:
                spacing 15

                text "Subject: Quick Assistance Needed" size 28 color "#000000"
                text "From: director.hale@aethernet.co" size 22 color "#444444"

                null height 15

                text  "Hi [player_name]" size 24 color "#000000"

                text "I need you to purchase 10 digital gift cards (₹5000 each) immediately." size 24 color "#000000"

                text  "I’ll reimburse through Finance." size 24 color "#000000"

                text "This is time-sensitive and confidential. Do not loop in anyone else." size 24 color "#000000"

                null height 10

                