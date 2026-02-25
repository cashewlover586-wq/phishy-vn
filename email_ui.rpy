screen email_ui():

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

                textbutton "Hover Over Link":
                    text_size 24
                    action [Return(), Jump("email_1_hover")]

                textbutton "Verify Sender":
                    text_size 24
                    action [Return(), Jump("email_1_verify")]

                textbutton "Report Phishing":
                    text_size 24
                    action [Return(), Jump("email_1_report")]

                textbutton "Mark Legitimate":
                    text_size 24
                    action [Return(), Jump("email_1_legit")]


        # RIGHT SIDE - EMAIL CONTENT
        frame:
            xsize 900
            ysize 600
            padding (40,40)
            background "#ffffff"

            vbox:
                spacing 15

                text "Subject: Action Required: Password Expiration Notice" size 28 color "#000000"
                text "From: IT Support <it-support@aethrnet-security.com>" size 22 color "#444444"

                null height 15

                text "Our records indicate that your AetherNet credentials are scheduled to expire within the next 60 minutes." size 24 color "#000000"

                text "To avoid account suspension, confirm your login details using the secure portal below:" size 24 color "#000000"

                null height 10

                textbutton "https://aethrnet-security.com/verify-account":
                    text_size 24
                    text_color "#0066cc"
                    action Jump("clicked_fake_link")

                null height 10

                text "Failure to verify may result in temporary deactivation." size 24 color "#000000"



            