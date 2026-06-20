# Introduction to Ad-hoc Charge Request Advice

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/CGSWMX/International_PaymentsCBPR/CGSWMX/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Charge Request Advice > Introduction

- Charge Request Advice;)
  - [Introduction](../../International_PaymentsCBPR/CGSWMX/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/CGSWMX/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/CGSWMX/Working_with.htm)
  - [Tasks](../../International_PaymentsCBPR/CGSWMX/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/CGSWMX/Outputs.htm)

Payments

# Introduction to Ad-hoc Charge Request Advice

Updated On 09 January 2025 |
 2 Min(s) read

Feedback
Summarize

The Charge Request Advice (CGSWMX) module manages a wide range of interbank ad-hoc charge transactions. The CGSWMX product license enables the users to capture the following types of transactions:

- Request charges from other financial institutions.
- Advise financial institutions about charges booked to their accounts.
- Book the charges to the accounts - For TPH embedded with Transact clients only.

Charge Request Advice integrates with the Delivery framework and generates the messages Charges Payment Notification Message - camt.105/MT190/290 or Charges Payment Request Message - camt.106/MT191/291/991, to facilitate the communication of charge-related transactions, not previously known to the receiver. Under SWIFT CBPR, the MX is not yet mandatory for these camt message types and therefore the system allows the user to decide if they want to send the MT or the MX. The ability to send the MX messages requires the rulebook CBPR24 or higher rulebook to be activated.

The **Charges Payment Notification Message (camt.105)** or **MT190/MT290** are sent by the account servicing institution to the account owner to advise previously unknown charges being applied to the owner's account.

The **Charges Payment Request Message (camt.106)** or **MT191/MT291** are sent by a financial institution to another financial institution to request the payment of charges which are previously unknown to the receiver.

The Charge Request Advice (CGSWMX) can be implemented along Standalone TPH or TPH embedded with Transact, the PP and PI modules are pre-requisites.

In the context of Transact embedded with TPH and depending on the option selected, the booking can be raised for the respective charges/commissions and the related tax, ensuring that all ad-hoc charge transactions are recorded and reflected in the books of the financial institution.

In this topic

- [Introduction to Ad-hoc Charge Request Advice](#IntroductiontoAdhocChargeRequestAdvice)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:59:53 PM IST