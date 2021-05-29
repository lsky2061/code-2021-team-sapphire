library(shiny)
library(reticulate)
library(dplyr)
library(shiny)
library(shinythemes)
library(shinyBS)
library(shinyjs)
library(shinycssloaders)
ui <- function(input, output){(navbarPage("SmartPA",
                   
                   tabPanel(
                       "Claim Prediction",
                       
                       sidebarLayout(
                           sidebarPanel(
                               tags$head(tags$script('
                                     Shiny.addCustomMessageHandler("myCallbackHandler",
                                       function(typeMessage) {console.log(typeMessage)
                                          if(typeMessage == 1){
                                          console.log("got here");
                                          $("a:contains(Select Resolution)").click();
                                          }
                                          if(typeMessage == 2){
                                          $("a:contains(Select Data range)").click();
                                          }
                                          });
                                          ')),
                               h3("Claim Prediction"),
                               # set panel width
                               width = 8,
                               
                               # about pop-up page
                               actionButton("about", "About CoverMyMed"),
                               # show help message
                               actionButton("help_initial", "Help!"),
                               
                               
                               # horizontal line ----
                               tags$hr(),
                               
                               # horizontal line ----
                               tags$hr(),
                               
                               # parameter_tabs,
                               selectInput("Payer", label = h3("Payer"),
                                           c("417380", "417614", "417740","999001")),br(),
                               selectInput("Drug", label = h3("Drug"),
                                           c("A", "B", "C")),br(),
                               
                               
                               # horizontal line ----
                               tags$hr(),
                               actionButton("Cal", "Formulary"),
                               textOutput("successrate"),
                               tags$head(tags$style("#successrate{color: blue;
                                 display:block;
                                bottom: -40px; 
                                position:absolute;
                                width: 100%;
                                left:50px;
                                 font-size: 20px;
                                 font-style: italic;
                                 }"
                               )
                               )
                           ),
                           mainPanel(
                               
                               
                           )
                       ),
                       bsModal(id="welcome", title = "Welcome to CoverMyMeds!", trigger="about", size="large",
                               "CoverMyMeds, part of McKesson's Prescription Technology Solutions, is a fast-growing
healthcare technology company that has been recognized as a “Best Place to Work” by
Glassdoor and a “Best Company to Work For” by FORTUNE. CoverMyMeds’ solutions
help patients get the medications they need to live healthy lives by seamlessly
connecting the healthcare network to improve medication access", tags$br(), tags$br(),
                               "At CoverMyMeds, one of our products is an
electronic PA (ePA) solution that replaces a largely manual process of looking for the
relevant form, printing it, filling it out, and faxing it to a simple portal-based experience.", tags$br(), tags$br(),
                               "This app is develope to perform three functions: Predict if a medical claim will be approved; Calculate the ePA approval rate based on the statistics of our medical data; Predict if an ePA will be approved based on our machine learning models. "),
                       tags$footer(
                           "CoverMyMeds App Contributors: Yiming Gong, Luke Corwin, Katherine Zhang, Prerna Kabtiyal",
                           align = "center", style = "
    position:fixed;
    bottom:0;
    width:100%;
    height:50px;
    color: white;
    padding: 10px;
    background-color: black;
    z-index: 1000;"
                       )
                       
                       
                   ),
                   tabPanel(
                       "ePA Prediction with Statistics",
                       
                       sidebarLayout(
                           sidebarPanel(
                               # set panel width
                               tags$head(tags$script('
                                     Shiny.addCustomMessageHandler("myCallbackHandler",
                                       function(typeMessage) {console.log(typeMessage)
                                          if(typeMessage == 1){
                                          console.log("got here");
                                          $("a:contains(Select Resolution)").click();
                                          }
                                          if(typeMessage == 2){
                                          $("a:contains(Select Data range)").click();
                                          }
                                          });
                                          ')),
                               h3("ePA Prediction with Statistics"),
                               width = 8,
                               
                               # about pop-up page
                               actionButton("about1", "About CoverMyMed"),
                               # show help message
                               actionButton("help_initial1", "Help!"),
                               # horizontal line ----
                               tags$hr(),
                               # horizontal line ----
                               tags$hr(),
                               
                               selectInput("correct_diagnosis", label = h3("Correct_diagnosis"),
                                           c(0, 1)),br(),
                               selectInput("tried_and_failed", label = h3("Tried_and_failed"),
                                           c(0, 1)),br(),
                               selectInput("contraindiction", label = h3("Contraindiction"),
                                           c(0, 1)),br(),
                               selectInput("binn", label = h3("Payer"),
                                           c(417380, 417740,999001,417614)),br(),
                               selectInput("drug", label = h3("Drug"),
                                           c("A", "B","C")),br(),
                               selectInput("reject_code", label = h3("Reject_code"),
                                           c(76.0, 75.0, 70.0)),br(),
                               fluidRow(column(5,
                                               actionButton("Cal_PA", "The approval rate of my PA?")
                               ),
                               column(5, ofset = 3,
                                      textOutput("PAsuccessrate"),
                                      tags$head(tags$style("#PAsuccessrate{color: blue;
                                 display:block;
                                bottom: -40px; 
                                position:absolute;
                                width: 100%;
                                left:50px;
                                 font-size: 20px;
                                 font-style: italic;
                                 }"
                                      )
                                      )
                               )),
                               
                               # horizontal line ----
                               tags$hr()
                               
                               
                               
                               
                               
                               
                           ),
                           
                           mainPanel(
                               
                           )
                       ),
                       bsModal(id="welcome1", title = "Welcome to CoverMyMeds!", trigger="about1", size="large",
                               "CoverMyMeds, part of McKesson's Prescription Technology Solutions, is a fast-growing
healthcare technology company that has been recognized as a “Best Place to Work” by
Glassdoor and a “Best Company to Work For” by FORTUNE. CoverMyMeds’ solutions
help patients get the medications they need to live healthy lives by seamlessly
connecting the healthcare network to improve medication access", tags$br(), tags$br(),
                               "At CoverMyMeds, one of our products is an
electronic PA (ePA) solution that replaces a largely manual process of looking for the
relevant form, printing it, filling it out, and faxing it to a simple portal-based experience.", tags$br(), tags$br(),
                               "This app is develope to perform three functions: Predict if a medical claim will be approved; Calculate the ePA approval rate based on the statistics of our medical data; Predict if an ePA will be approved based on our machine learning models. "),
                       tags$footer(
                           "CoverMyMeds App Contributors: Yiming Gong, Luke Corwin, Katherine Zhang, Prerna Kabtiyal",
                           align = "center", style = "
    position:fixed;
    bottom:0;
    width:100%;
    height:50px;
    color: white;
    padding: 10px;
    background-color: black;
    z-index: 1000;"
                       )
                       
                   ),
                   
                   tabPanel(
                       "ePA Prediction with Machine Learning",
                       
                       sidebarLayout(
                           sidebarPanel(
                               # set panel width
                               tags$head(tags$script('
                                     Shiny.addCustomMessageHandler("myCallbackHandler",
                                       function(typeMessage) {console.log(typeMessage)
                                          if(typeMessage == 1){
                                          console.log("got here");
                                          $("a:contains(Select Resolution)").click();
                                          }
                                          if(typeMessage == 2){
                                          $("a:contains(Select Data range)").click();
                                          }
                                          });
                                          ')),
                               h3("ePA Prediction with Machine Learning"),
                               width = 8,
                               
                               # about pop-up page
                               actionButton("about2", "About CoverMyMed"),
                               # show help message
                               actionButton("help_initial2", "Help!"),
                               # horizontal line ----
                               tags$hr(),
                               
                               selectInput("payer_PA", label = h3("Payer"),
                                           c(417380, 417614, 417740,999001)),
                               selectInput("drug_PA", label = h3("Drug"),
                                           c("A", "B","C")),br(),
                               selectInput("correct_diagnosis_PA", label = h3("Correct_diagnosis"),
                                           c(0, 1),width = "220px"),br(),
                               selectInput("tried_and_failed_PA", label = h3("Tried_and_failed"),
                                           c(0, 1),width = "220px"),br(),
                               selectInput("contraindiction_PA", label = h3("Contraindiction"),
                                           c(0, 1)),br(),
                               selectInput("not_in_formulary_PA", label = h3("Not_in_formulary"),
                                           c(0, 1)),br(),
                               selectInput("limit_exceeded_PA", label = h3("Limit_exceeded"),
                                           c(0, 1)),br(),
                               
                               fluidRow(column(5,
                                               actionButton("PA_machine", "Will my PA get approved?",height = "2px")
                               ),
                               column(5, ofset = 3,
                                      textOutput("PAsuccessrate_ML"),
                                      tags$head(tags$style("#PAsuccessrate_ML{color: blue;
                                display:block;
                                bottom: -30px; 
                                position:absolute;
                                width: 100%;
                                left:50px;
                                 font-size: 20px;
                                 font-style: italic;
                                 }"
                                      )
                                      )
                               )),
                               
                               # horizontal line ----
                               tags$hr()
                               
                           ),
                           
                           mainPanel(
                               
                           ),
                       ),
                       bsModal(id="welcome2", title = "Welcome to CoverMyMeds!", trigger="about2", size="large",
                               "CoverMyMeds, part of McKesson's Prescription Technology Solutions, is a fast-growing
healthcare technology company that has been recognized as a “Best Place to Work” by
Glassdoor and a “Best Company to Work For” by FORTUNE. CoverMyMeds’ solutions
help patients get the medications they need to live healthy lives by seamlessly
connecting the healthcare network to improve medication access", tags$br(), tags$br(),
                               "At CoverMyMeds, one of our products is an
electronic PA (ePA) solution that replaces a largely manual process of looking for the
relevant form, printing it, filling it out, and faxing it to a simple portal-based experience.", tags$br(), tags$br(),
                               "This app is develope to perform three functions: Predict if a medical claim will be approved; Calculate the ePA approval rate based on the statistics of our medical data; Predict if an ePA will be approved based on our machine learning models. "),
                       
                       tags$footer(
                           "CoverMyMeds App Contributors: Yiming Gong, Luke Corwin, Katherine Zhang, Prerna Kabtiyal",
                           align = "center", style = "
    position:fixed;
    bottom:0;
    width:100%;
    height:50px;
    color: white;
    padding: 10px;
    background-color: black;
    z-index: 1000;"
                       )
                       
                   )
))}
# # FIXME: change it to your local virtual environment
# reticulate::use_virtualenv("~/env")
# reticulate::use_python('~/Desktop/interpreter/bin/python')
# source_python('claim_approval.py')
VIRTUALENV_NAME = "env_example"
# # -----------shiny-----------------
# Sys.setenv(PYTHON_PATH = '~/Desktop/interpreter/bin/python')
# Sys.setenv(VIRTUALENV_NAME = VIRTUALENV_NAME) # Installs into default shiny virtualenvs dir
# Sys.setenv(RETICULATE_PYTHON = '~/Desktop/interpreter/bin/python')
# # -----------shiny-----------------


#Sys.setenv(PYTHON_PATH = 'python3')
#Sys.setenv(VIRTUALENV_NAME = VIRTUALENV_NAME) # Installs into default shiny virtualenvs dir
#Sys.setenv(RETICULATE_PYTHON = paste0('/home/shiny/.virtualenvs/', VIRTUALENV_NAME, '/bin/python'))


# Define any Python packages needed for the app here:

PYTHON_DEPENDENCIES = c('numpy', 'autocorrect==2.1.0', 'boto3', 'botocore', 'certifi', 'chardet', 'click', 'future', 'gensim==3.8.3', 'idna', 'itsdangerous', 'jmespath', 'joblib', 'MarkupSafe', 'nltk==3.5', 'numpy','pandas','python-dateutil','pytz','rake-nltk','regex','s3transfer','six','smart-open','threadpoolctl','tqdm','Werkzeug', 'sklearn', 'scikit-learn')

count = 0




server <- function(input, output, session) {
    
    # Expression that generates a plot of the distribution. The expression
    # is wrapped in a call to renderPlot to indicate that:
    #
    #  1) It is "reactive" and therefore should be automatically
    #     re-executed when inputs change
    #  2) Its output type is a plot
    # Create virtual env and install dependencies
    # has_env = Sys.getenv('HAS_ENV')
    # virtualenv_dir = paste0('/home/shiny/.virtualenvs/', VIRTUALENV_NAME, '/bin/python')
                            # python_path = Sys.getenv('PYTHON_PATH')

                            reticulate::virtualenv_create(envname = "python35_env", python = "python3")
                            reticulate::virtualenv_install("python35_env", packages = PYTHON_DEPENDENCIES, ignore_installed=TRUE)

                            
                            reticulate::use_virtualenv("python35_env", required = T)
                            reticulate::source_python('claim_approval.py')
                            # add ids for all notifications and removeNotification() when compute button is pressed
                            help_initial_id <- NULL
                            observeEvent(input$help_initial, {
                                help_initial_id <<- showNotification(
                                    # helpText("HELP: Upload a csv file with your data. Then, choose whether to summarize the text data. If not summarizing the data, select an obfuscation level. Finally, click the compute button to get your obfuscated data.",
                                    helpText("HELP: Choose the payer you are applying to. Then, choose the drug you are requesting. Click the Formulary button to know if your drug is in the formulary and if you will need a PA.",
                                             style="color:#3E4649;"),
                                    duration=120, type=c("warning"))
                            }) #observeEvent
                            
                            observeEvent(input$select_Data, {
                                updateTabsetPanel(inputId = "params", selected = input$select_Data, session = session)
                            }) #observeEvent
                            
                            chosenLevel <- reactive(input$level)
                            chosendata <- reactive(input$select_Data)
                            chosenSummarize <- reactive(input$summarize)
                            chosendrugs <- reactive(input$Drug)
                            chosenpayer <- reactive(input$Payer)
                            chosencorrect_diagnosis <- reactive(input$correct_diagnosis)
                            chosentried_and_failed <- reactive(input$tried_and_failed)
                            chosencontraindiction <- reactive(input$contraindiction)
                            chosenbinn <- reactive(input$binn)
                            chosendrug <- reactive(input$drug)
                            chosenreject_code <- reactive(input$reject_code)
                            chosenPayer_ML <-reactive(input$Payer_PA)
                            chosendrug_ML <-reactive(input$Drug_PA)
                            chosencorrect_diagnosis_ML <-reactive(input$correct_diagnosis_PA)
                            chosentried_and_failed_ML <-reactive(input$tried_and_failed_PA)
                            chosencontraindiction_ML <-reactive(input$contraindiction_PA)
                            chosenformulary_ML <-reactive(input$not_in_formulary_PA)
                            chosenlimit_ML<-reactive(input$limit_exceeded_PA)
                            
                            
                            
                            observeEvent(input$help_initial1, {
                                help_initial_id <<- showNotification(
                                    helpText("HELP: A code 70 implies that a drug is not covered by the plan and is not on formulary. Code 75 implies that a drug is on the formulary but does not have preferred status and
requires a prior authorization (PA).A code 76 simply means that the drug is covered, but that the plan
limitations have been exceeded. Click the approval rate of my PA button to know the approval rate of your PA.",
                                             style="color:#3E4649;"),
                                    duration=120, type=c("warning"))
                            })
                            observeEvent(input$help_initial2, {
                                help_initial_id <<- showNotification(
                                    # helpText("HELP: Upload a csv file with your data. Then, choose whether to summarize the text data. If not summarizing the data, select an obfuscation level. Finally, click the compute button to get your obfuscated data.",
                                    helpText("HELP: Click the Will my PA get approved button to know the prediction from our machine learning model.",
                                             style="color:#3E4649;"),
                                    duration=120, type=c("warning"))
                            })
                            observeEvent(input$Cal, {
                                if (!is.null(help_initial_id))
                                    removeNotification(help_initial_id)
                                help_initial_id <<- NULL
                                
                                
                                output$successrate <- renderText({
                                    
                                    paste(InFormulary(chosenpayer(),chosendrugs()))
                                })
                            })
                            
                            observeEvent(input$Cal_PA, {
                                if (!is.null(help_initial_id))
                                    removeNotification(help_initial_id)
                                help_initial_id <<- NULL
                                
                                output$PAsuccessrate <- renderText({
                                    
                                    paste(pa_approval(chosencorrect_diagnosis(),chosentried_and_failed(),chosencontraindiction(),chosenbinn(),chosendrug(),chosenreject_code()))
                                })
                            })
                            observeEvent(input$PA_machine, {
                                if (!is.null(help_initial_id))
                                    removeNotification(help_initial_id)
                                help_initial_id <<- NULL
                                
                                output$PAsuccessrate_ML <- renderText({
                                    
                                    paste( ePAApprove(chosenPayer_ML(),chosendrug_ML(),chosencorrect_diagnosis_ML(),chosentried_and_failed_ML(),chosencontraindiction_ML(),chosenformulary_ML(),chosenlimit_ML()))
                                })
                            })
}
# Run the application 
shinyApp(ui = ui, server = server)
