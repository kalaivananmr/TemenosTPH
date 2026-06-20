# Introduction to SWIFT SSI File Upload

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSSIU/International_PaymentsCBPR/PPSSIU/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT SSI File Upload > Introduction

- SWIFT SSI File Upload;)
  - [Introduction](../../International_PaymentsCBPR/PPSSIU/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSSIU/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSSIU/Workingwith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSSIU/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSSIU/Outputs.htm)

Payments

# Introduction to SWIFT SSI File Upload

Updated On 27 May 2024 |
 4 Min(s) read

Feedback
Summarize

The system provides multiple options to route outgoing and redirected cross border payments using contract definition. The system allows to configure the following types of contracts:

| Contract | Description |
| --- | --- |
| Party Contract | The party contract is checked for the credit party in the payment. In a party contract, the bank specifies on how the payment should be routed and settled with the credit party. |
| Country Contract | The country contract is checked for the destination country of the payment. In a country contract, the bank specifies on how it wants to route and settle payments to be sent to a specific country. |
| Bank Level Contract | The default bank level contract is applied if a corresponding country and party contract is not found. |

While processing an outgoing or redirected payment, if a relevant contract is not found then it is a set up issue and the payment is routed to repair. The system provides the following options using which banks can define the contract. If routing cannot be determined, then the system checks if Alternative for Routing and Settlement failure is configured otherwise the payment is moved to repair.

The possible routing options are

- Loro or Nostro Relationship
- Country Correspondent
- Currency Correspondent
- Relationship between Head office and Branch
- Account for Settlement

Read [Routing SWIFT International Payments](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#Routing) to know more about the routing options.

## License

The bank must have a PP license as part of the Routing and Settlement (R&S) selection of currency correspondent. In addition, the bank must also have a PPSSIU license for uploading SSI files. Read [SWIFT MX](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) for more information.

The SSIPlus file is migrated to the SSI directory as part of the new SWIFTRef products. The SSI directory contains the RELATIONSHIPS-SSI file that holds the Standing Settlement Instructions (SSI) for all related combinations of *Account Owner*, *Currency*, and *Asset Category*. TPH system provides an option to upload the SSI data from both SSIPlus and RELATIONSHIPS-SSI files.

Routing SWIFT International Payments

Based on the currency of the payment, the creditor bank can have a currency correspondent. The currency correspondents are released by SWIFT as part of the Standing Settlement Instructions file.

For example, if a payment in USD needs to be routed to Deutsche Bank in Germany and the RS rules are set in such a way that the creditor bank can be reached through its currency correspondent, then the RS module should determine the currency correspondent for Deutsche Bank and route the payment through the bank.

[](#)[Currency Correspondent](#)

The system has the ability to store a Currency Correspondent per country. The bank can define more than one currency correspondent per country. The user can configure the routing rules to send a payment using the currency correspondent.

In this topic

- [Introduction to SWIFT SSI File Upload](#IntroductiontoSWIFTSSIFileUpload)

- [License](#License)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:55:34 PM IST