# Introduction to SWIFT MX Cheques

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSWCQ/International_PaymentsCBPR/PPSWCQ/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT MX Cheques > Introduction

- SWIFT MX Cheques;)
  - [Introduction](../../International_PaymentsCBPR/PPSWCQ/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSWCQ/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSWCQ/Workingwith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSWCQ/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSWCQ/Outputs.htm)

Payments

# Introduction to SWIFT MX Cheques

Updated On 22 March 2025 |
 7 Min(s) read

Feedback
Summarize

The CBPR+ (Cross-Border Payments and Reporting Plus) working group is responsible for defining the MX message formats and usage guidelines (available in the SWIFT CBPR+ portal).

Temenos Payments Hub supports the processing of cross-border international payments using SWIFT MX (ISO20022) messages. This document explains the processing of the ISO message “Cheque Presentment Notification” Camt.107.

The Cheque Presentment Notification message is sent by a drawer bank, to the bank on which a cheque has been drawn (the drawee bank). It is used to advise the drawee bank, the details concerning the cheque referred to in the message. The Cheque Presentment Notification is restricted to a single cheque per InterAct message.

CBPR+ camt.107 messages are used for this purpose. The equivalent message in SWIFT FIN is MT110.

## Message Types

The following table lists the SWIFT CBPR+ messages supported by Temenos Payments Hub system for Cheque Presentment Notification. Read [SWIFT MX](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) for more information.

| ISO20022 MX  Message | Payment Order Type | MT Equivalent | Module Code | Outward | Inward | Redirect | Business Service |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Camt.107.001.01 | Cheque Presentment Notification | MT110 | PPSWCQ | ü | × | × | swift.cbprplus.01 |

## Payment Types

The system supports the following types of cross border international payment

| Payment Type | Description |
| --- | --- |
| Foreign Currency cheques | FCY cheque is issued by drawer bank at the request of the payer favouring payee (Beneficiary).   - Swift supports ChequePresentmentNotification, that is, the message is sent by a drawer bank or a bank acting on behalf of the drawer bank to the bank on which a cheque has been drawn (the drawee bank). - camt.107 is the SWIFT CBPR+ message used for ChequePresentmentNotification. - ChequePresentmentNotification is restricted to a single cheque per message. |

## Configurable Support for SWIFT MT or MX format to Send Cross Border Payments

The following table shows the outgoing message format for cross border customer payments captured or initiated from the system.

| Company Configuration | Message Direction | Outgoing Message Type |
| --- | --- | --- |
| Company configured to send cross border payments in MX format | Outgoing | CBPR+camt.107 ( cheque presentation Notification |
| Company configured to send cross border payments in MX format at a future date | Outgoing | CBPR+camt.107 ( cheque presentation Notification on or after future date |
| Company configured to send cross border payments in MT format | Outgoing | MT110 (Advice of Cheques) |

## CBPR+ Payment Capture through Payment Order

The front office users can capture outgoing cross border international payment using the PAYMENT.ORDER (`PO`) application. The system provides a dedicated menu to capture payments. The following screens have the relevant ISO20022 fields.

- CBPR+ Customer Transfer – On successful processing, outgoing CBPR+ pacs.008 message is generated
- CBPR+ Bank Transfer – On successful processing, outgoing CBPR+ pacs.009 message is generated
- CBPR+ ChequePresentationNotification: A bank user can initiate a foreign currency (FCY) draft request favouring payee (Beneficiary) based on payer's (TPH customer) instruction. On successful processing, outgoing CBPR+ camt.107 message is generated

Dedicated payment order products are provided for CBPR+ customer and bank transfer.

## Cheque Presentment Notification

The ChequePresentmentNotification message is sent by a drawer bank to the bank where the cheque has been drawn (the drawee bank). It is used to advise the drawee bank of the details concerning the cheque referred to in the message. ChequePresentmentNotification is restricted to a single cheque per InterAct message.

The CBPR+ camt.107 message is used for this purpose. The equivalent message in SWIFT FIN is MT110.

The following section explains the support for this message in the system.

[Generation of Outgoing camt.107](#)

The ChequePresentmentNotification message informs the drawee agent about the cheque submission. The notification message facilitates the drawee agent to follow up on the cheque submission and relevant business process.

When these FCY draft issuance messages are processed successfully, the system generates CBPR+ camt.107 and sends it to the drawee bank. To generate camt.107, the following conditions must be satisfied:

- The bank requires a PPSWCX license in addition to a PPSWMX license.
- Current SWIFT MX installed in the bank must be greater or equal to the year when cheques CBPR+ camt.107 (2023) were live on SWIFT FINPLUS.
- TPH bank has an agreement with the drawee bank to send camt.107
- Drawer bank must maintain a Nostro account with the drawee bank. If the Nostro account is not available, the payment message is routed to the repair queue.
- RMA is to be maintained with the drawee bank to send a camt.107 message. If RMA is not available, the payment message is routed to the repair queue.
- Format validations for camt.107 are successful. If validations are not successful, the payment is routed to the repair queue.
- A message should be sent before the cut-off time, else, the payment is routed to the repair queue.

- If TPH bank has an agreement with the drawee bank to send both MT110 and camt.107, then camt.107 is given the first preference if all the conditions stated above are satisfied.
- If no SWIFT cheque advice is defined (MT110 or camt.107), then only accounting entries are raised in the system without sending a notification message to the drawee bank.

The CBPR+ camt.107 message is generated and sent to SWIFT through the delivery module. The status of the FCY draft payment in the system is updated like an outgoing payment settled serially (based on whether acknowledgment or DLN will be received). Users can view the outgoing camt.107 messsages from the Pending and Processed enquiry.

[Acknowledgments and Exceptions](#)

If a positive technical acknowledgement is received (indicating SWIFT has accepted the message), the Current State in Payment Order moves to ‘AwaitingPrinting’, that is, the system is ready for printing the draft. If a negative acknowledgment is received, the system does not perform any automatic action. The user can view all outgoing messages using the ‘SWIFT ISO Technical Exception’ enquiry and perform manual actions on the underlying message. Read the [Technical Acknowledgement Processing](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#Technica) section for more information.

If the XSD validation fails in TPH during message transformation to XML format, this message cannot be sent out. The users can try manually. Read the [Action on Non-Payments Failing XSD Validation in Temenos Payments Hub Transformation Layer](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#202305)  section for more details.

In this topic

- [Introduction to SWIFT MX Cheques](#IntroductiontoSWIFTMXCheques)

- [Message Types](#MessageTypes)
- [Payment Types](#PaymentTypes)
- [Configurable Support for SWIFT MT or MX format to Send Cross Border Payments](#ConfigurableSupportforSWIFTMTorMXformattoSendCrossBorderPayments)
- [CBPR+ Payment Capture through Payment Order](#CBPRPaymentCapturethroughPaymentOrder)
- [Cheque Presentment Notification](#ChequePresentmentNotification)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:53:22 PM IST