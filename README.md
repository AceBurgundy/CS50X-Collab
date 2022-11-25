
# Collab

A simple project collaboration web app/bug tracker that documents and lets a team keep track of bugs on their software. A work in progress. c. 2022

Also my final project for CS50 Intro to Computer Science.

#### Video Demo: [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YnjgDPM061I/0.jpg)](https://www.youtube.com/watch?v=YnjgDPM061I)

## Tree

```
Collab                                                 
├─ app.py                                              
├─ collab.db                                           
├─ License                                             
├─ README.md                                           
└─ Tracker                                             
   ├─ collab.db                                        
   ├─ config.py                                        
   ├─ errors                                           
   │  ├─ handlers.py                                   
   │  ├─ static                                        
   │  │  └─ errors                                     
   │  │     └─ errors.css                              
   │  ├─ templates                                     
   │  │  └─ errors                                     
   │  │     └─ apology.html                            
   │  └─ __init__.py                                   
   ├─ helpers.py                                       
   ├─ index                                            
   │  ├─ static                                        
   │  │  └─ index                                      
   │  │     ├─ head.css                                
   │  │     ├─ head.js                                 
   │  │     ├─ index.css                               
   │  │     ├─ index.js                                
   │  │     ├─ navigation-rail.css                     
   │  │     └─ project.js                              
   │  ├─ templates                                     
   │  │  └─ index                                      
   │  │     ├─ head.html                               
   │  │     ├─ index.html                              
   │  │     └─ layout.html                             
   │  ├─ views.py                                      
   │  └─ __init__.py                                   
   ├─ models.py                                        
   ├─ profile                                          
   │  ├─ forms.py                                      
   │  ├─ static                                        
   │  │  └─ profile                                    
   │  │     ├─ changePassword.css                      
   │  │     ├─ country-dropdown-styles.css             
   │  │     ├─ profile.css                             
   │  │     └─ profile.js                              
   │  ├─ templates                                     
   │  │  └─ profile                                    
   │  │     ├─ newPassword.html                        
   │  │     └─ profile.html                            
   │  ├─ views.py                                      
   │  └─ __init__.py                                   
   ├─ projects                                         
   │  ├─ forms.py                                      
   │  ├─ static                                        
   │  │  └─ projects                                   
   │  │     └─ project.css                             
   │  ├─ templates                                     
   │  │  └─ projects                                   
   │  │     └─ project-modal.html                      
   │  ├─ views.py                                      
   │  └─ __init__.py                                   
   ├─ static                                           
   │  ├─ background.css                                
   │  ├─ flags                                         
   │  ├─ fonts                                         
   │  │  ├─ Poppins-Medium.ttf                         
   │  │  ├─ Rubik-Light.ttf                            
   │  │  ├─ Rubik-Medium.ttf                           
   │  │  ├─ Rubik-Regular.ttf                          
   │  │  └─ Salin-medium.otf                           
   │  ├─ fonts.css                                     
   │  ├─ form-modal.css                                
   │  ├─ form-modal.js                                 
   │  ├─ helper.js                                     
   │  └─ root.css                                      
   ├─ tickets                                          
   │  ├─ forms.py                                      
   │  ├─ static                                        
   │  │  └─ tickets                                    
   │  │     ├─ ticket-details.css                      
   │  │     ├─ ticket-details.js                       
   │  │     ├─ ticket.js                               
   │  │     └─ tickets.css                             
   │  ├─ templates                                     
   │  │  └─ tickets                                    
   │  │     ├─ comment.html                            
   │  │     ├─ like.html                               
   │  │     ├─ ticket-details.html                     
   │  │     ├─ ticket-modal.html                       
   │  │     └─ tickets.html                            
   │  ├─ views.py                                      
   │  └─ __init__.py                                   
   ├─ user                                             
   │  ├─ forms.py                                      
   │  ├─ static                                        
   │  │  └─ user                                       
   │  │     ├─ login.js                                
   │  │     ├─ register.js                             
   │  │     └─ user-styles.css                         
   │  ├─ templates                                     
   │  │  └─ user                                       
   │  │     ├─ login.html                              
   │  │     └─ register.html                           
   │  ├─ views.py                                      
   │  └─ __init__.py                                   
   └─ __init__.py                                      

```
## Features

### App
- simple but beautiful UI

### Projects
- Create Projects
- Collaborate with other creators
- Edit project

### Tickets
- Kanban project management
- Cross platform (incomplete)
- Comment on tickets


## Authors

- [@AceBurgundy](https://github.com/AceBurgundy)

- [@AACaps](https://github.com/AACaps) (Contributors)