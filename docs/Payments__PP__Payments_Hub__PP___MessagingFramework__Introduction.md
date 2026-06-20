# Introduction to Messaging Framework

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/MessagingFramework/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Temenos Payments Hub > Messaging Framework

- Temenos Payments Hub;)
  - [Introduction](../../Payments_Hub_(PP)/Misc/Introduction.htm)
  - [Messaging Framework Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Introduction.htm)
    - [Inward Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Intro_Inward.htm)
    - [Outward Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Intro_Outward.htm)
  - Clearing;)
  - Sanction Screening;)
  - Status Reporting;)
  - Cheque Clearing;)
  - Code Words;)
  - Direct Debits;)
  - International Payments (MT);)
  - Manual Repair;)
  - Business Dates;)
  - Posting;)
  - Fees and Billing;)
  - Funds Reservation;)
  - Warehousing;)
  - Book Transfer;)
  - Investigations and Enquiries;)
  - Routing and Settlement;)
  - Business Validations;)
  - Static Data;)
  - Standalone Payments;)
  - [Standalone Implementation Options Standalone Implementation Options](../../Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm)
  - Forex;)
  - Bulk Payments;)
  - Bank Condition;)
  - Client Condition;)
  - Product Determination;)
  - Housekeeping Functions;)
  - FATF and WTR2;)
  - PSD2;)
  - SWIFT gpi;)
  - SWIFT Universal Confirmations;)
  - Instant Payments;)
  - Agency Banking;)
  - Returns and Reversal;)
  - Exceptions and Investigations;)
  - Clearing Status Report;)
  - Monitoring;)
  - Counterparty Risk;)

Payments

# Introduction to Messaging Framework

Updated On 22 March 2025 |
 2 Min(s) read

Feedback
Summarize

Temenos Payments Hub uses messaging framework as a integrated component to support all types of messages. Messaging Framework deals with validation, transformation, mapping and handling of the messages (XML, non-XML).

- XML - Can be ISO20022 based or proprietary
- Non-XML – Text based formats that are fixed length records or with field de-limiters

Once the messages are mapped, the Temenos Payments Hub processing engine processes the payments and books the payment or generates outgoing messages specific to the target system (such as, Clearing).

The framework can be configured to support any Clearing or external system. It is built using Apache Camel open-source integration framework and is available as an out-of-the-box solution.

The following are the two parts of Messaging Framework.

- [Inward Messaging Framework](Intro_Inward.htm)
- [Outward Messaging Framework](Intro_Outward.htm)

TPH Messaging Framework can receive RtP messages from an Instant Payments Clearing. The RtP messages received are routed to the RtP module for processing.

Read TPH Messaging Framework Installation Guide to know more technical details of the [Messaging Framework](../../../../../Installation/Payments_TPH_Messaging_Installation/TPH_Messaging_Framework_Install_Guide/MISC/Overview.htm).

In this topic

- [Introduction to Messaging Framework](#IntroductiontoMessagingFramework)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:52:26 PM IST