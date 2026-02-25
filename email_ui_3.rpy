screen email_ui_3():

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
                    action [Return(), Jump("email_3_verify")]

                textbutton "Open Attachment Preview":
                    text_size 24
                    action [Return(), Jump("clicked_link_3")]

                textbutton "Report Phishing":
                    text_size 24
                    action [Return(), Jump("email_3_report")]

                textbutton "Mark Legitimate":
                    text_size 24
                    action [Return(), Jump("email_3_legit")]


        # RIGHT SIDE - EMAIL CONTENT
        frame:
            xsize 900
            ysize 600
            padding (40,40)
            background "#ffffff"

            vbox:
                spacing 15

                text "Subject: Invoice #78421 – Q1 Software Licensing" size 28 color "#000000"
                text "From: finance@aethernet-support.com" size 22 color "#444444"

                null height 15

                text  "Please find attached Invoice #78421 for Q1 software licensing renewal." size 24 color "#000000"

                text "Process payment before the due date to avoid service interruption." size 24 color "#000000"

                text  "Attachment:" size 24 color "#000000"

                null height 10

                textbutton "Invoice_78421.pdf":
                    text_size 24
                    text_color "#0066cc"
                    action Jump("clicked_link_3")

                null height 10

                