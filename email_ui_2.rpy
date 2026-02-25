screen email_ui_2():

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
                    action [Return(), Jump("email_2_hover")]

                textbutton "Verify Sender":
                    text_size 24
                    action [Return(), Jump("email_2_verify")]

                textbutton "Report Phishing":
                    text_size 24
                    action [Return(), Jump("email_2_report")]

                textbutton "Mark Legitimate":
                    text_size 24
                    action [Return(), Jump("email_2_legit")]


        # RIGHT SIDE - EMAIL CONTENT
        frame:
            xsize 900
            ysize 600
            padding (40,40)
            background "#ffffff"

            vbox:
                spacing 15

                text "Subject: Updated Agenda – Security Briefing (Today 3 PM)" size 28 color "#000000"
                text "From: hr@aethernet.com" size 22 color "#444444"

                null height 15

                text  "Good morning," size 24 color "#000000"

                text "Today's Security Briefing has been moved to 3:00 PM due to a scheduling conflict." size 24 color "#000000"

                text  "Updated agenda available here:" size 24 color "#000000"

                null height 10

                textbutton "https://portal.aethernet.com/security-briefing":
                    text_size 24
                    text_color "#0066cc"
                    action Jump("clicked_link_2")

                null height 10

                text "Attendance is mandatory for all new analysts." size 24 color "#000000"