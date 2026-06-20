# Configuring Interac Instant Payment via Central1

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Canada/Canada/PPCAIC/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Regional Framework > Canada Model Bank > Interac Instant Payment via Central1 > Configuration

- Regional Framework;)
  - Canada Model Bank;)
    - Interac Instant Payment via Central1;)
      - [Introduction](../../Canada/PPCAIC/Introduction.htm)
      - [Configuration](../../Canada/PPCAIC/Configuration.htm)
      - [Working with](../../Canada/PPCAIC/WorkingWith.htm)
      - [Tasks](../../Canada/PPCAIC/Tasks.htm)
      - [Outputs](../../Canada/PPCAIC/Outputs.htm)

Payments

# Configuring Interac Instant Payment via Central1

Updated On 04 March 2025 |
 3 Min(s) read

Feedback
Summarize

The following configurations are available for the Interac Instant Payment via Central1 module.

## Configuring Account Number Validation

Local clearing setup is required as prerequisites.

Pre-Requisite

With the Upgrade to JDK 21, the following configuraton must to be done in Java Opts.

```
(-Djdk.xml.xpathExprGrpLimit=0 -Djdk.xml.xpathExprOpLimit=0 -Djdk.xml.xpathTotalOpLimit=0)
```

Copy

As part of this development, an API has to be attached as a hook routine to format the account number received from Interac and store in TPH .

[Configurations Released by Temenos](#)

The following configuration records are provided and maintained by Temenos out of the box. The bank should not setup or change the records below.

[Configure the PP.MSGMAPPINGPARAMETER Application](#)

1. Configure the Interac account numbering *Enrich API* to the PP.MSGMAPPINGPARAMETER application as per below.



[Configurations Required](#)

The following configurations are required for the Account Number Validation functionality.

[Configure the PP.IN.CHANNELS Application](#)

1. Configure the BATCH record from the PP.IN.CHANNELS application to indicate the queue name and path to place the file.



## Configuring Interac eTransfer

The configurations in application.properties are required for this functionality.

## Configuring Interac Instant Payment Clearing

This section will allow users to better understand the configurations for the Interac Instant Payment Clearing functionality.

[Configurations Released by Temenos](#)

The following configuration records are provided and maintained by Temenos out of the box. The bank should not setup or change the records below.

[PP.IN.ENTRY.PARAM Configuration](#)

1. The PPCAIC.GENERATE.ACK.NACK.MSG validation routine was attached to the *Fieldname* field in the PP.IN.ENTRY.PARAM application so that a positive or negative response will be sent to C1. Based on posting response ok or Nok, the pacs.002 response will be triggered.



[PP.CLEARING Configuration](#)

1. The *Ack Type For Bene Bank* field from the PP.CLEARING application was configured as Confirmationmessage.



[PP.CLEARING.SETTING Configuration](#)

1. The following PP.CLEARING.SETTING records are released out of the box:
   - C1INTRC.CAD.R.pacs.002.
   - C1INTRC.CAD.S.pacs.002.
   - C1INTRC.CAD.R.pacs.007.
   - C1INTRC.CAD.R.pacs.008.
   - C1INTRC.CAD.R.pacs.004.
   - C1INTRC.CAD.R.pacs.003.
2. A sample of the C1INTRC.CAD.R.pacs.002 record is provided below.



In this topic

- [Configuring Interac Instant Payment via Central1](#ConfiguringInteracInstantPaymentviaCentral1)

- [Configuring Account Number Validation](#ConfiguringAccountNumberValidation)
- [Configuring Interac eTransfer](#ConfiguringInteraceTransfer)
- [Configuring Interac Instant Payment Clearing](#ConfiguringInteracInstantPaymentClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:00:25 PM IST