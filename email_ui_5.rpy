screen email_ui_5():

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
                    action [Return(), Jump("email_5_hover")]

                textbutton "Verify URL structure carefully":
                    text_size 24
                    action [Return(), Jump("email_5_verify")]

                textbutton "Enter Credentials":
                    text_size 24
                    action [Return(), Jump("email_5_enter")]

                textbutton "Report as Phishing":
                    text_size 24
                    action [Return(), Jump("email_5_report")]
                
                textbutton "Access portal through official bookmarked site":
                    text_size 24
                    action [Return(), Jump("email_5_bookmark")]
                    


        # RIGHT SIDE - EMAIL CONTENT
        frame:
            xsize 900
            ysize 600
            padding (40,40)
            background "#ffffff"

            vbox:
                spacing 15

                text "Subject: Security Sync Required – Token Validation" size 28 color "#000000"
                text "From: security@aethernet.com" size 22 color "#444444"

                null height 15

                text  "All analysts must validate access tokens before 5:00 PM." size 24 color "#000000"

                textbutton "https://portal-aethernet.com/validate-session":
                    text_size 24
                    text_color "#0066cc"
                    action Jump("clicked_link_5")

                text  "This process takes less than 60 seconds." size 24 color "#000000"

                text "Token Validation Window: [final_timer] seconds remaining." size 24 color "#000000"

                null height 10

                