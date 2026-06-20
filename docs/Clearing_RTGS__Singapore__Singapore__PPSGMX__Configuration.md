# Configuring SGMEPS Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Singapore/Singapore/PPSGMX/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Singapore > SGMEPS in ISO20022 (MX) > Configuration

- Singapore;)
  - SGMEPS in ISO20022 (MX);)
    - [Introduction](../../Singapore/PPSGMX/Introduction.htm)
    - [Configuration](../../Singapore/PPSGMX/Configuration.htm)
    - [Working with](../../Singapore/PPSGMX/WorkingWith.htm)
    - [Tasks](../../Singapore/PPSGMX/Tasks.htm)
    - [Outputs](../../Singapore/PPSGMX/Outputs.htm)

Payments

# Configuring SGMEPS Clearing

Updated On 12 April 2026 |
 7 Min(s) read

Feedback
Summarize

This section details with the Configuration/Parameterisation for the feature. Any mentions to no-change fields, implementation considerations based on the configuration options and type of file, should be added here.

This section will allow users to better understand the configurations for the Singapore MEPS Clearing module.

## Pre-Configurations:

The following pre-configurations are required for the Singapore MEPS Clearing module.

Make sure the latest .xslt files are available in the Stylesheet folder, as per below.

The user should ensure whether the following highlighted files are available in the path location.

1. Stylesheet 

2. Camel wars



   Camel Wars



   Camel Wars



   Camel Wars



   Camel Wars

   Slide 1

   Slide 2

   Previous SlideNext Slide
3. XSD
   Make sure the following .xsd files are available in the **XSDs > SGMEPSCT** folder.



   XSD



   XSD



   XSD



   XSD



   XSD

   Slide 1

   Slide 2

   Slide 3

   Previous SlideNext Slide

## Configurations Required for Customer and Bank transfer

The following configurations are required for the Singapore MEPS Clearing module.

[Configure the PP.CLEARING.SETTING Application](#)

- Go to the **Admin Menu > Payments > Payment Hub > Bank System Administration > Local Clearing > Clearing Setting** menu.
  Configure the *SGMEPS.SGD.\*.S.pacs.008-<SYSTEM.TODAY>* record Clearing Account Number, Suspense Account Number in the **PP.CLEARING.SETTING** application as shown below:



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING
- Configure the *SGMEPS.SGD.\*.S.pacs.009-<SYSTEM.TODAY>* record Clearing Account Number, Suspense Account Number in the **PP.CLEARING.SETTING** application as shown below:



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING
- Configure the *SGMEPS.SGD.\*.R.pacs.008.CT-<SYSTEM.TODAY>* record Clearing Account Number, Suspense Account Number in the **PP.CLEARING.SETTING** application as shown below:



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING
- Configure the *SGMEPS.SGD.\*.R.pacs.009.CT-<SYSTEM.TODAY>* record Clearing Account Number, Suspense Account Number in the **PP.CLEARING.SETTING** application as shown below:



  PP.CLEARING.SETTING



  PP.CLEARING.SETTING

[Configure the RD.CENTRAL.BANK.DIR Application](#)

Configure the bank's BIC in the RD.CENTRAL.BANK.DIR application as per the samples given below:



[Configure the PP.CONTRACT Application](#)

Configure the PP.CONTRACT application as shown below:



PP.CONTRACT




PP.CONTRACT

[Configure the PP.CONTRACT Application](#)

Go to the **Admin Menu > Payments > Payment Hub > Bank Operations Configuration > Routing and Settlement > R&S Rules Definition** menu. Configure the *PP.CONTRACT* application as per the samples given below:



PP.CONTRACT




PP.CONTRACT

[Configure the PP.RMA Application](#)

Configure the PP.RMA application, set Message Type as per the samples given below:



PP.RMA




PP.RMA




PP.RMA

[Configure the PAYMENT.ORDER.PRODUCT Application](#)

1. Go to the **Admin Menu > Payments > Payment Order > Payment Order Product Setup** menu.
2. The *MEPSBT* record has been configured and set ValidateAPI as **PPSGMX.VALIDATE.API.FOR.POA**.

[Configure the EB.API Application](#)

The **PPSGMX.VALIDATE.API.FOR.POA** record has been configured as shown below:



## Configurations Required for pacs.009 COV

The following configurations are required for the Singapore MEPS Cover payment

[Configure the DE.DISTINGUISH.NAME.RULES Application](#)

Configure the **CBPRPLUS.RULE1** record has been configured as shown below:



[Configure the DE.CARRIER Application](#)

1. Go to the **Admin Menu > Framework Parameter > Delivery > DeliveryParams > Carrier** menu.
2. Configure the **DE.CARRIER SGMEPS** record as shown below:



   DE.CARRIER SGMEPS



   DE.CARRIER SGMEPS

[Configure the DE.PARAM Application](#)

1. Go to the **Admin Menu > Framework Parameter > Delivery > DeliveryParams > PARAM** menu.
2. Configure the **DE.PARAM** record as shown below:

[Configure the PP.CLEARING Application](#)

1. Go to the **Admin Menu > Payments > Payment Hub > Bank System Administration > Local Clearing > Clearing** menu.
2. Configure the **PP.CLEARING** SwiftBased as MX for SGMEPS.



   PP.CLEARING



   PP.CLEARING.COMPANY

[Configure the PP.COMPANY.PROPERTIES Application](#)

1. Go to the **Admin Menu > Payments > Payment Hub > Bank System Administration > Static Data > Company Properties** menu.
2. Configure the **PP.COMPANY.PROPERTIES** application as shown below:

[Configure the IF.INTEGRATION.SERVICE.PARAM Application](#)

Configure the SYSTEM record in the **IF.INTEGRATION.SERVICE.PARAM** application as shown below:



[Configure the DE.INTERFACE Application](#)

Configure the **ALLIANCEINTERACT** record in the **DE.INTERFACE** application as shown below



[Configure the PP.RMA Application](#)

Configure the PP.RMA application as shown below:



PP.RMA



PP.RMA

[Configure the PP.STANDINGSETTMNTINSTRUC Application](#)

Configure the **PP.STANDINGSETTMNTINSTRUC** application as shown below:



[Configure the PP.CONTRACT Application](#)

1. Go to the **Admin Menu > Payments > Payment Hub > Bank Operations Configuration > Routing and Settlement > R&S Rules Definition** menu.
2. Configure the **PP.CONTRACT** application as shown below:



   PP.CONTRACT



   PP.CONTRACT



   PP.CONTRACT

### Configure the PP.RMA Application

- To ensure pacs\*, camt\* is present in the Messagetypeinclude field of the PP.RMA application record.


### Configure the DE.PARM Application

- Go to the **Admin Menu > Framework Parameter > Delivery > Delivery Param** menu.
- Set the *Payment System* as TPS in the **SYSTEM.STATUS** record.


### Configure the PP.COMPANY.PROPERTIES Application

- Go to the **Admin Menu > Payments > Payment Hub > Bank System Administration > Static Data > Company Properties** menu.
- Set the *Holdforcovermethod* field as Cover, *Coversuspenseaccountcategory* field as 10001 and *Gpienabledbank* field as Y.


### Configure the PP.LORO.NOSTRO.ACCOUNT Application

- Loro nostro account for DEMOGBPX and InstgAgt’s BIC should be created as per the samples below.



### Configure the ER.PARAMETER Application

- Make sure both account numbers are defined in the **SYSTEM** record of the **ER.PARAMETER** application.
- In the incoming message, InstgAgt’s BIC nostro account number and Clearing setting’s clearing account number should be configured in ER.PARAMETER application
- Remove raw xml if present


### Configure the CA.CLEARING.DIRECTORY.PARAM Application

- Go to the **Admin Menu > Payments > Clearing Directory > Clearing Directory Parameter** menu.
- Configure the **SGMEPS.CT**. record in the **CA.CLEARING.DIRECTORY.PARAM** application, where the Reachability Key Fields are set to National Clr Code, Payment Channel. The Reachability Api will be set with the generic reachability API name.


### Configure the CA.CLEARING.DIRECTORY Application

- Go to the **Admin Menu > Payments > Clearing Directory > Clearing Directory** menu.

### Configure the QueueConfig.properties

1. The following configurations are required for Inward SGMEPS payments.
2. Add the following lines of code to the existing QueueConfig.properties file if it does not already exist.

   ```
   ClearingInput1=SGMEPSMX
   TPH.CLEARING1.INPUT.QUEUE=SGMEPSMX
   SGMEPSMX-XSDValidationRequired=TRUE
   SGMEPSMX-ClearingMsgFormat=XML
   SGMEPSMX-RTGSSystem=TRUE
   SGMEPSMX-AppendQueueNameToXSDandXSLT=TRUE
   SGMEPSMX-DE=TRUE
   ```

   Copy

### Configure the QueueConfigCT.properties

1. The following configurations are required for Outward SGMEPS payments.
2. Add the following lines of code to the existing QueueConfigCT.properties file if it does not already exist.

   ```
   QUEUE-SGMEPS=ClearingOutQueue1
   ClearingOutFolder1=SGMEPSOutput
   ClearingOutQueue1=TPH.SGMEPS.CT.OUT.QUEUE
   SGMEPS-XSDValidation=True
   #Added as part of MEPS Cover Enhancement
   mas.mep.cov.01=COV
   SGMEPS-DE=TRUE
   ```

   Copy

## Configurations to Support Extended Characters

Following are the configurations required to support extended characters.

1. Ensure that the following configurations are available in the ASCII.VALUES record.


2. Ensure that the DE.MSG.CHARS.RULE and PP.CHAR.CONVERSION records are available for the pacs.008, pacs.008 STP, pacs.009, and pacs.009 COV message types.

## Configurations to Support Usage Identifier

To support usage identifier, ensure the following configurations are available in DE.BUSINESS.SERVICE.RULES.









In this topic

- [Configuring SGMEPS Clearing](#ConfiguringSGMEPSClearing)

- [Pre-Configurations:](#PreConfigurations)
- [Configurations Required for Customer and Bank transfer](#ConfigurationsRequiredforCustomerandBanktransfer)
- [Configurations Required for pacs.009 COV](#ConfigurationsRequiredforpacs009COV)
- [Configurations to Support Extended Characters](#ConfigurationstoSupportExtendedCharacters)
- [Configurations to Support Usage Identifier](#ConfigurationstoSupportUsageIdentifier)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:08:14 PM IST