# This program is for removing @*** stuff from emails
email=["matsn@optonline.net","shawnce@icloud.com","stecoop@live.com","rmcfarla@yahoo.com","parrt@gmail.com","cmdrgravy@msn.com","ralamosm@yahoo.com","mccurley@att.net"]
for i in range(0,len(email)-1):
  i_email=str(email[i])
  a=i_email.index("@")   # This program is for removing @*** stuff from emails
  print(i_email[0:a])
