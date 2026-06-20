# Configuring NEFT Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/India/India/PPINNP/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Regional Framework > India Model Bank > NEFT Clearing > Configuration

- Regional Framework;)
  - India Model Bank;)
    - NEFT Clearing;)
      - [Introduction](../../India/PPINNP/Introduction.htm)
      - [Configuration](../../India/PPINNP/Configuration.htm)
      - [Working with](../../India/PPINNP/WorkingWith.htm)
      - [Tasks](../../India/PPINNP/Tasks.htm)
      - [Outputs](../../India/PPINNP/Outputs.htm)
    - RTGS Clearing;)

Payments

# Configuring NEFT Clearing

Updated On 08 November 2022 |
 6 Min(s) read

Feedback
Summarize

The following applications were introduced with this module. Below you can find details on the menu item name associated to each application. The menu name will be used throughout the documentation.

| Application Name | Model Bank Menu Item Name | Used By | Description |
| --- | --- | --- | --- |
| PAYMENT.ORDER,INDIA.NEFT | PO.INPUT.REGION.INDIA **(National Electronic Fund Transfer - NEFT)** | Business Users | This version is used to initiate a national electronic fund transfer request. |

This section will allow users to better understand the configurations for the NEFT Clearing module.

## Configurations Released by Temenos

The following configuration records are provided and maintained by Temenos out of the box. The bank should not setup or change the records below.

[PP.CLEARING Application Configuration](#)

1. The PP.CLEARING application has been configured as per below.



[PP.CLEARING.SETTING Application Configuration](#)

1. The PP.CLEARING.SETTING application has been configured as per below.





[PP.LIGHTWEIGHTPRODUCTCOND Application Configuration](#)

1. The following records have been created in the PP.LIGHTWEIGHTPRODUCTCOND application.



[PP.MSG.ACCEPTANCE.PARAM Application Configuration](#)

1. The PPINNP.ENRICH.GENERIC.XML API has been attached in the PP.MSG.ACCEPTANCE.PARAM application.



[PP.MSGMAPPINGPARAMETER Application Configuration](#)

1. The PP.MSGMAPPINGPARAMETER application has been configured as per below.



[PP.SOURCE.SETTING Application Configuration](#)

1. The *Automated Cancel Indicator* field has been set to N in the POA record from the PP.SOURCE.SETTING application.



[RD.CENTRAL.BANK.DIR Application Configuration](#)

1. The RD.CENTRAL.BANK.DIR application has been configured as per below.



[PP.SPECIFIC.WEIGHT Application Configuration](#)

1. The PP.SPECIFIC.WEIGHT application has been configured as per below.



[PP.CLEARING.COMPANY Application Configuration](#)

1. The PP.CLEARING.COMPANY application has been configured as per below.



[PAYMENT.ORDER.PRODUCT Application Configuration](#)

1. The *Validate API* and the *Lei Trshld Amt* fields have been configured in the INDNEFT record from the PAYMENT.ORDER.PRODUCT application as per below.



[pain.001 Configurations](#)

1. The TPHCTI record from the `PP.MSG.ACCEPTANCE.PARAM` application has been configured as per below.


2. The IPI record from the `PP.CHANNEL` application has been configured as per below.


3. The IPI record from the `PP.SOURCEPRODUCTGROUP` application has been configured as per below.


4. The IPI record from the `PP.SOURCE` application has been configured as per below.


5. The IPI.pain.001 record from the `PP.MSGMAPPINGPARAMETER` application has been configured as per below.


6. The IPI.pain.001.R record from the `PP.MSG.FORMAT.PER.CHANEL` application has been configured as per below.


7. The IPI.pain.001.CT record from the `PP.SPECIFIC.WEIGHT` application has been configured as per below.


8. The INDNEFT record from the `PP.CLEARING` application has been configured as per below.


9. The INDNEFT.O.PAIN.001 .D record from the `PP.HEAVYWEIGHTPRODUCTCOND` application has been configured as per below.



[EB.API Application Configuration](#)

1. The `EB.API` application has been configured as per below.



[EB.FILE.UPLOAD.TYPE Application Configuration](#)

The `EB.FILE.UPLOAD.TYPE` application stores the definition of the file uploads based on which the files will be uploaded by Temenos Transact.

1. The INDCLRGDIR record from the `EB.FILE.UPLOAD.TYPE` application has been configured as per below.


2. The INDNEFTCRS record from the `EB.FILE.UPLOAD.TYPE` application has been configured as per below.



[EB.FILE.UPLOAD.PARAM Application Configuration](#)

A file folder named INDCLRGDIR has been created under the directory mentioned in the `EB.FILE.UPLOAD.PARAM` application for the SYSTEM record. The folder name is the same as the one entered in the *Upload Dir* field from the `EB.FILE.UPLOAD.TYPE` application.

1. To enable the automatic upload of the India RTGS or NEFT participant directory, a text file, named information file (with any filename, for example INDCLRGDIR.xml) has been created in the folder specified in the `EB.FILE.UPLOAD.PARAM` application.



[BATCH Application Configuration](#)

1. The `BATCH` application has been configured as per below.



[CA.CLEARING.DIRECTORY.PARAM Application Configuration](#)

1. The INDNEFT and INDRTGS records have been configured in the `CA.CLEARING.DIRECTORY.PARAM` application where the reachability key fields have been set to IFSC and the payment channel. The reachability API has been set with the generic reachability API name.


2. The upload program will update the below-mentioned fields in the `CLEARING.DIRECTORY.PARAM` application every time a new India RTGS or NEFT participant directory file is uploaded. After upload, two records will be created for a IFSC code, one for NEFT and RTGS separately with the IFSC details.
   - *Last Source File Name:* Displays the name of the most recent uploaded file.
   - Last Upload Date.
   - *Last Effective Date* (system date).

[`CA.CLEARING.DIRECTORY` Application Configuration](#)

1. The INDNEFTHDFC record has been configured in the `CA.CLEARING.DIRECTORY` application as per below.



## Configurations Required

The following configurations are required for the NEFT Clearing module.

[Configure the PP.COMPANY.PROPERTIES Application](#)

1. Set the *NationaId* field from the PP.COMPANY.PROPERTIES application.


2. Set the *No Bic Bk cd Validation* field to Y.



[Configure the RD.CTRY.NAT.SYS.IDENTIFIER Application](#)

1. Configure the RD.CTRY.NAT.SYS.IDENTIFIER application as per below for IFSC validation.



[Configure the F.PP.COMPONENT.API.HOOK!DateDetermination.json File](#)

1. Configure the F.PP.COMPONENT.API.HOOK!DateDetermination.json file as per below.



[Configure the PP.MEDIUMWEIGHTPRODUCTCOND Application Configuration](#)

1. The *Non STP Indicator* field has to be set to Y in the INDNEFT.O.POA.I / INDNEFT.O.POA.D record from the PP.MEDIUMWEIGHTPRODUCTCOND application.



[Configure the EB.LOOKUP Application](#)

1. The *Data Value* needs to be configured as 2, 4 or 6 during the implementation based on the client requirements.



[Configure the `PP.ERRORTYPES` Application](#)

1. Configure the `PP.ERRORTYPES` application as per below.



[Configure the `PI.ERROR.REASON.CODE` Application](#)

1. Use the `PI.ERROR.REASON.CODE` application to configure the required error codes.



In this topic

- [Configuring NEFT Clearing](#ConfiguringNEFTClearing)

- [Configurations Released by Temenos](#ConfigurationsReleasedbyTemenos)
- [Configurations Required](#ConfigurationsRequired)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:04:05 PM IST