# Introduction to Request to Pay

> Source: https://docs.temenos.com/docs/Solutions/Payments/Request_to_Pay/SAIPS/RTP_Clearing/Saudi_Arabia_RFPYSA/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Saudi Arabia > Saudi Arabia Instant Payment System (SAIPS) – Request to Pay > Introduction

- Saudi Arabia;)
  - Saudi Arabia Instant Payment System (SAIPS) – Request to Pay;)
    - [Introduction](../../RTP_Clearing/Saudi_Arabia_RFPYSA/Introduction.htm)
    - [Configuration](../../RTP_Clearing/Saudi_Arabia_RFPYSA/Configuration.htm)
    - [Working with](../../RTP_Clearing/Saudi_Arabia_RFPYSA/WorkingWith.htm)
    - [Tasks](../../RTP_Clearing/Saudi_Arabia_RFPYSA/Tasks.htm)
    - [Outputs](../../RTP_Clearing/Saudi_Arabia_RFPYSA/Outputs.htm)

Payments

# Introduction to Request to Pay

Updated On 08 November 2022 |
 6 Min(s) read

Feedback
Summarize

Saudi payments introduced Instant Payments System (IPS) to accelerate business transactions and move towards a cashless society, which is central to the development of the financial sector. IPS provides core Clearing and Settlement Mechanism (CSM) and associated Value-Added Services (VAS) in support of payment and payment-related transactions. The IPS Central Infrastructure (CI) provides real-time message processing and 24x7 payment clearing capabilities.

The faster payment platform allows immediate and scheduled transfers (in real-time) between various banks in the kingdom. It also provides greater flexibility for businesses to add payment details and instructions to the beneficiary. This helps to execute transactions between companies efficiently and verifies beneficiaries to facilitate financial settlement.

The Saudi Payments RtP system enables a Payee/Requestor (Creditor) to request a payment towards a Payer (Debtor) for the exchange of services or goods. The payer can decide to approve or decline the request resulting in authorization (or refusal) of the payment transaction. Upon approval of the request, the payment is processed and the payment is credited to the Requestor. If the request is declined, the payer bank sends back the information to the payee or requestor bank.

[Participant Types](#)

Direct Member: A member bank that sends message and payments directly to Saudi IPS clearing. Each direct member is provided with a participant ID (IPS participant) which is useful in sending RtP messages.

[Outward Processing](#)

The outward processing (Initiation) of the RtP is described below.



| Activity | | Description |
| --- | --- | --- |
| Accept and Enrich | | The system accepts and enriches the RtP request from the payee or requestor with source file, message Id, and so on, and maps into the RtP system |
| Validations: During the initiation of RtP, the user need to perform certain validations so that the payment following the request does not result in an error | | |
| Requestor Validation | | Debtor Account number/IBAN – Either debtor account number or IBAN must be available  Creditor Account number/IBAN – Either creditor account number or IBAN must be available |
| Scheme Validation | | Request scheme should be Saudi Payment RtP scheme  Currency - Validate against allowed currency in RtP scheme. The currency should be ‘SAR’ |
| Other Validation | | Account status and Restriction Check – Validate the Credit Account/IBAN status and check if any restrictions placed in the account  Date validation – The Requested execution date should be less or equal to the expiry date. If Expiry date is not present then requested execution date will be considered as the Expiry date.  Duplicate check – If enabled the request is validated for any duplicate of the message  Instructed amount – The amount should be greater than zero |
| Proxy Resolution | | The proxy provided is resolved and the required details of the payee or requestor are fetched. For example, mobile number can be used as Proxy/Alias for the payee or requestor, which is resolved by DDA and required IBAN details are fetched. For Native accounts the Proxy/Alias is resolved internally |
| Generate RTP request | | An RtP request is generated through a pain.013 message |
| Error | | Errors during the process are notified to the payee or requestor for correction |

[Inward Processing](#)

The following flowchart describes the Inward processing (reception) of RtP.



| Activity | | Description |
| --- | --- | --- |
| Validations | | The incoming message is validated against the given message structure. The validations include scheme and Business validations. |
| Scheme validation | | Incoming request scheme should be Saudi Payment RTP scheme.  Currency – Validate against allowed currency in RTP scheme. The currency should be ‘SAR’  Payment Method – The allowed payment method should be ‘TRF’ |
| Business validation | | Received Date time – Should be always less than expiry date  Payer BIC / NCC – validated against BIC/NCC in RP parameter  Account number / IBAN validation – validate if the account number / IBAN exists  Credit Account number / IBAN – validate if IBAN or account number is provided |
| Acknowledgement to RTP service | | If the Incoming RtP request is validated successfully and presented to the payer, then an acknowledgement is sent to the payee or requestor |
| Park for customer consent | | The Request is processed further only when payer acts upon it. The payer can provide the consent before the expiry date after which the RtP request expires |
| RtP acceptance Ack to payee or requestor | | Interim response is generated when the payer decides to pay on a future date. The generation of Interim acceptance message generation is an optional feature |
| Generate Payment request | | The payment request is generated in the `PAYMENT.ORDER (PO)` application and sent to the payment system (TPH or any other payment system) to process the payment |
| Receive payment completion response | | The payment completion response is communicated from the payment system (TPH or any other payment system) to RtP system through `PO` application |
| RtP final acceptance to payee or requestor | | Once the payment is complete, the payment completion status is communicated to the payee or requestor through pain.014 message |

In this topic

- [Introduction to Request to Pay](#IntroductiontoRequesttoPay)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:28:37 PM IST