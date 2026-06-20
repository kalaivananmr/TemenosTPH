# APIs - Pp

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/APIs/Misc/APIs.htm#PP

---

2. [Payments](../../../../content/payments.html)

- Temenos Payments Hub;)

Payments

# APIs

Updated On 06 October 2023 |
 8 Min(s) read

Feedback
Summarize

The Temenos Provider APIs expose Temenos product business capabilities as RESTful (Representational state transfer) APIs defined in the OpenAPI Specification (OAS).

## CLEARING ACCESSIBILITY (CA)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-payments-service-v3.0.0 | Manages the enquire on the payments that were processed or under processing online banking channels or bank host system. APIs also offer a limited set of maintenance of the payments, such as for example Recalling the payment. | GET |
| 2 | order | order-payments-service-v3.2.0 | Manages the enquire on the payments that were processed or under processing online banking channels or bank host system. APIs also offer a limited set of maintenance of the payments, such as for example Recalling the payment. | GET |

## PAYMENT INITIATION (PI)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-paymentOrders-service-v1.0.0 | Creates and manages payment orders, creates Sepa and Swift payment records. | PUT, POST, DELETE, GET |
| 2 | order | order-paymentOrders-service-v2.0.0 | Creates and manages payment orders, creates Sepa and Swift payment records. | PUT, POST, DELETE, GET |
| 3 | order | order-paymentOrders-service-v2.1.0 | Creates and manages payment orders, creates Sepa and Swift payment records. | PUT, POST, DELETE, GET |
| 4 | order | order-paymentOrders-service-v2.2.0 | Creates and manages payment orders, creates Sepa and Swift payment records and transparency cehck details from payment order to infinity. | PUT, POST, DELETE, GET |
| 5 | order | order-paymentOrders-service-v2.3.0 | Creates and manages payment orders, creates Sepa and Swift payment records and transparency cehck details from payment order to infinity. | PUT, POST, DELETE, GET |
| 6 | order | order-paymentsConfiguration-service-v1.0.0 | Updates the parameter that connects payment order and payment system, and payment features specific to a product. This API is depreacted. Use the following instead. URL:/settings/configuration/payments/products/{productId} | PUT |
| 7 | reference | reference-BICs-service-v1.0.0 | Retrieves BIC details.Thsi API is depcrated. Use /reference/bankCodes/bics/{bicId} from BICS-service-V3.0.0 instead. | GET |
| 8 | reference | reference-IBANs-service-v1.0.0 | Retrieves IBANs details. | GET |
| 9 | settings | settings-paymentsConfiguration-v1.0.0 | Creates and manages default configurations for payment orders. | POST, PUT, GET |
| 10 | order | order-paymentOrders-service-v3.2.0 | Manages the payment orders before they are being sent for payment execution by the bank's payment system. It provides order management functionality for payers to initiate, view and manage their orders from an online channel offered by payer's bank or authorized third party. Temenos Order Application(POA) lists the APIs offered by Temenos payment order application to perform order management for payers. | GET |
| 11 | order | order-paymentOrders-service-v3.3.0 | Manages the payment orders before they are being sent for payment execution by the bank's payment system. It provides order management functionality for payers to initiate, view and manage their orders from an online channel offered by payer's bank or authorized third party. Temenos Order Application(POA) lists the APIs offered by Temenos payment order application to perform order management for payers. | POST, DELETE, PUT |
| 12 | order | order-paymentOrders-service-v3.4.0 | Manages the payment orders before they are being sent for payment execution by the bank's payment system. It provides order management functionality for payers to initiate, view and manage their orders from an online channel offered by payer's bank or authorized third party. Temenos Order Application(POA) lists the APIs offered by Temenos payment order application to perform order management for payers. | POST, DELETE, PUT |
| 13 | order | order-paymentOrders-service-v4.0.0 | Manages the payment orders before they are being sent for payment execution by the bank's payment system. It provides order management functionality for payers to initiate, view and manage their orders from an online channel offered by payer's bank or authorized third party. Temenos Order Application(POA) lists the APIs offered by Temenos payment order application to perform order management for payers. | POST, DELETE, PUT |

## TEMENOS PAYMENT (PP)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | meta | meta-payments-service-v2.0.0 | Retrieves the payment transaction api query filters. | GET |
| 2 | order | order-paymentOrders-service-v1.0.0 | Creates, updates and retrieves GPI payment status. | POST, PUT, GET |
| 3 | order | order-paymentOrders-service-v2.0.0 | Creates and updates a GPI payment status with unique transaction reference. | POST, PUT |
| 4 | order | order-paymentOrders-service-v2.1.0 | Creates and updates a GPI payment status with unique transaction reference. | POST, PUT |
| 5 | order | order-paymentOrders-service-v2.2.0 | Creates and updates a GPI payment status with unique transaction reference. | POST, PUT |
| 6 | order | order-paymentOrders-service-v2.3.0 | Creates and updates a GPI payment status with unique transaction reference. | POST, PUT |
| 7 | order | order-payments-service-v1.0.0 | Creates and manages payments and transfers. | GET |
| 8 | order | order-payments-service-v2.0.0 | Retrieves and updates payment details and payment transactions. | GET, PUT |
| 9 | order | order-payments-service-v3.0.0 | Retrieves the list of reason codes and displays it to the customer. | GET |
| 10 | order | order-paymentUserAgents-service-v3.0.0 | Retrieves ISO customer and bank payments transaction content. | GET |
| 11 | order | updatePpSoTransactionApi-v1.0.0 | Updates `PP.SO.TRANSACTION`. This API is deprecated and moved to the following URL : /payments/swiftPayments/{swiftPaymentId}/acknowledgements | PUT |
| 12 | order | UpdatePSMBLOBApi-v1.0.0 | Updates PSM BLOB. This API is deprecated and moved to the following URL : payments/logs/sentMessages/{sentMessageId} | PUT |
| 13 | settings | settings-paymentsConfiguration-v1.0.0 | Creates and manages payment configurations. | GET, PUT, POST, DELETE |

## REQUEST TO PAY (RF)

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | RequestToPayPayments-v1.0.0 | Creates and manages Request to Pay payments in order to create, view, update, block and decline the payment requests from both biller and payer systems. Creates payment requests for EBA and UK scheme from biller application. | PUT, GET, POST |
| 2 | order | RequestToPayPayments-v1.3.0 | Updates accessToken and scheme for a specific proxy identifier which in turn triggers the refresh and updates Request To Pay(RTP) data store. | PUT |
| 3 | order | RequestToPayPayments-v1.4.0 | Manages the Temenos bank with their request to pay functionality. It provides RTP functionality and information exchange between the actor (payer or payee) and the RTP clearing. This page lists the APIs offered by Temenos RTP Application to consume and manage RTP functionality by payee and payer, who are typically accessing the application from a bank based online channel. | PUT, GET, POST |
| 4 | order | RequestToPayPayments-v1.6.0 | Manages the Temenos bank with their request to pay functionality. It provides RTP functionality and information exchange between the actor (payer or payee) and the RTP clearing. This page lists the APIs offered by Temenos RTP Application to consume and manage RTP functionality by payee and payer, who are typically accessing the application from a bank based online channel. | PUT, GET, POST |
| 5 | order | RequestToPayPayments-v1.7.0 | Manages the Temenos bank with their request to pay functionality. It provides RTP functionality and information exchange between the actor (payer or payee) and the RTP clearing. This page lists the APIs offered by Temenos RTP Application to consume and manage RTP functionality by payee and payer, who are typically accessing the application from a bank based online channel. | GET |
| 6 | order | RequestToPayPayments-v1.8.0 | Manages the Temenos bank with their request to pay functionality. It provides RTP functionality and information exchange between the actor (payer or payee) and the RTP clearing. This page lists the APIs offered by Temenos RTP Application to consume and manage RTP functionality by payee and payer, who are typically accessing the application from a bank based online channel. | GET |

## PAYMENTS EXTENSIBILITY

| S.No | Domain | API Name | Description | Method |
| --- | --- | --- | --- | --- |
| 1 | order | order-payments-service-v3.4.0 | - Retrieves and updates payment details in Order entry. - Creates and manages Payment extension message in order to create, view and update from the perimeter. | PUT, GET, POST |

In this topic

- [APIs](#APIs)

- [CLEARING ACCESSIBILITY (CA)](#CLEARINGACCESSIBILITYCA)
- [PAYMENT INITIATION (PI)](#PAYMENTINITIATIONPI)
- [TEMENOS PAYMENT (PP)](#TEMENOSPAYMENTPP)
- [REQUEST TO PAY (RF)](#REQUESTTOPAYRF)
- [PAYMENTS EXTENSIBILITY](#PAYMENTSEXTENSIBILITY)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:57:29 PM IST