# Introduction to Payments Extensibility

> Source: https://docs.temenos.com/docs/Solutions/Payments/Extensibility/Payments_Extensibility/Payments_Extensibility/Misc/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Payments Extensibility > Introduction

- Payments Extensibility;)
  - [Introduction](../../Payments_Extensibility/Misc/Introduction.htm)
  - [Configuration](../../Payments_Extensibility/Misc/Configuration.htm)
  - Local Clearing Extensions;)
  - Client Extensions;)

Payments

# Introduction to Payments Extensibility

Updated On 22 March 2025 |
 2 Min(s) read

Feedback
Summarize

Temenos Payments Hub provides an extensibility framework that empowers users to implement client specific developments to tailor existing features and enables local clearing implementation users to build new clearing processes. This framework is designed to handle all single payments (RTGS, SWIFT MX, ACH or Instant).

- Bulk (ACH) payments are not in scope for this phase.
- SWIFT MT messages are white-listed and hence can continue to use existing L3 Java hooks.

[Local Clearing Extension](#)

The extensibility framework allows users to create new local clearing processes tailored to their specific clearing needs. Users can define and implement these processes to ensure payments comply with local clearing standards, regional regulations, or other specific requirements.

[Client Extension](#)

The framework allows users to apply client specific business rules and validations to payments, ensuring that payments meet internal operational, legal, and regulatory requirements.

At the perimeter outside of TPH, the Local Clearing or Client specific user can enrich and validate payment attributes using the information in the transaction payload. In case payload information is insufficient and additional payment context is required (Temenos Payment's computed values for a payment), those can be ascertained using GET context Restful APIs to perform necessary validations and enrichments.

Such extensions are python scripts used at the perimeter, replacing TPH L3 JAVA API hooks. They can:

- Enrich incoming message payload
- Amend payment attribute during the straight-through message processing or when keyed in and repaired through Order Entry or initiated through Payment Order.
- Execute specialized validations and provide errors or warnings that might result in the need for manual intervention or automated exception processing of the payment.

The below diagram gives an overview of the entry and exit points in payment processing and where extensions can be built.



In this topic

- [Introduction to Payments Extensibility](#IntroductiontoPaymentsExtensibility)

Related topics:

- [APIs](../../APIs/Misc/APIs.htm#Exten)
- [Extending Transact APIs](https://docs.temenos.com/docs/Solutions/Technology/Extensibility_Framework/Extending_APIs/Extending_Transact_APIs/Misc/Extending_Transact_APIs.htm)
- [TPH Messaging Framework](https://docs.temenos.com/docs/Solutions/Installation/Payments_TPH_Messaging_Installation/TPH_Messaging_Framework_Install_Guide/MISC/Overview.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:43:07 PM IST