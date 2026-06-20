# Introduction to Saudi Arabia Instant Payments System (SAIPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SaudiArabia/SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Saudi Arabia > [Saudi Arabia Instant Payments System (SAIPS)](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm) > Introduction

- Saudi Arabia;)
  - [Saudi Arabia Riyal Interbank Express (SARIE) Saudi Arabia Riyal Interbank Express (SARIE)](../../SaudiArabia/Saudi_PPSARI/Introduction.htm)
  - [Saudi Arabia Instant Payments System (SAIPS) Saudi Arabia Instant Payments System (SAIPS)](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm)
    - [Introduction](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm)
    - [Configuration](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Configuration.htm)
    - [Working with](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Working_with.htm)
    - [Tasks](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Tasks.htm)
    - [Outputs](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Outputs.htm)

Payments

# Introduction to Saudi Arabia Instant Payments System (SAIPS)

Updated On 08 November 2022 |
 17 Min(s) read

Feedback
Summarize

Saudi payments is a wholly owned subsidiary of Saudi Arabian Monetary Authority (SAMA) that helps in:

- Developing a secure and interoperable national payment infrastructure by serving banks and fintechs equally
- Providing the required standardisation to ensure all providers have a level playing field

Saudi payments introduced Instant Payments System (IPS) to accelerate business transactions and move towards a cashless society, which is central to the development of the financial sector. IPS provides core Clearing and Settlement Mechanism (CSM) and associated Value-Added Services (VAS) in support of payment and payment-related transactions. The IPS Central Infrastructure (CI) provides real-time message processing and 24x7 payment clearing capabilities.

The faster payment platform allows immediate and scheduled transfers (in real-time) between various banks in the kingdom. It also provides greater flexibility for businesses to add payment details and instructions to the beneficiary. This helps to execute transactions between companies efficiently and verifies beneficiaries to facilitate financial settlement.

## Type of Participants

There is only direct participant in Saudi IPS customer payments.

| Type of Participant | Description |
| --- | --- |
| Direct Member | A participant bank that exchanges payments directly to the clearing and holds a settlement account with clearing. Payments can be initiated from TPH to a beneficiary through a direct participant. Direct participant bank is identified by the value ‘D’ in *Reachability Type* field in `CA.CLEARING.DIRECTORY`. |

## Outward Payment Processing



| Activity | Description |
| --- | --- |
| Manual capture of Saudi IPS payment from front office | - Captures a customer payment request through `PO` application (PAYMENT.ORDER, SARINST.INPUT.NEW) - Performs the following validations:   - *Debit Account IBAN*, *Debtor Name*, *Beneficiary IBAN*, *Beneficiary Name*, *Payment amount*, *Payment currency*, *Acct with Bank Clearing Code* are updated   - Either *Payment Purpose* or *Purpose Proprietary* is input   - *Transfer Currency Code* is SAR   - Bank account can have one of the direct participants, which is validated against `CA.CLEARING.DIRECTORY`   - Reachability check of creditor participant is based on TPH generic reachability with NCC as criteria   - Debit account does not have posting restriction   - Balance check on debit account   - IBAN validation on beneficiary’s account   - IBAN structure is same as SA IBAN structure. IBAN structure validation is done by referring to IBAN structure defined in `IN.IBAN.STRUCTURE` table   - Payment execution date is not back-dated   - Payment Purpose needs to have any of the following:     - BONU – Bonus payment     - DIVI – Dividend     - OTHR – Other payment     - SALA – Salary payment   - Purpose Proprietary needs to have any of the following:     - BEN – Military sector support     - CIT – Citizen account support     - MOF – Ministry of finance     - WEL – Ministry of finance   - Context name needs to have any of the following:     - Online banking     - Mobile banking     - Phone banking     - Branch     - Kiosk or ATM     - Corporate  If an error occurs during validation, it is displayed on the page for the user to correct or cancel the payment. If the error requires user intervention to complete the payment capture (such as insufficient balance in debit account), the user needs to override it to proceed. |
| Submission and supervisor approval | Performs validation on submission of the payments that awaits Supervisor’s approval:  - If approved, it moves the payment for further processing. - If rejected, it modifies and resubmits the payment for approval. |
| Debit authority | Checks whether debit authority is available for the debit account. |
| Debit party determination | Determines the debtor and enriches the payment transaction with details, such as name and address. |
| Debit bank condition check | Checks for an agreement with the debtor bank for special processing on the payment. If a valid agreement is available, the conditions are applied on the debit side of the payment. |
| Warehouse future dated | Warehouses the payment with future execution date and releases on Start of Date (SOD) of the execution date. |
| Balance check | Checks whether the debit account has enough funds to process the payment. |
| Product determination | Checks outward payments for configured payment products to find a match. If a match is not found, it displays an error. Payment product influences the processing of the following:   - Client-specific conditions - Routing - Fees - Filtering - Posting - Straight-Through Processing (STP) or manual processing |
| Debit client agreement check | Checks for an agreement with the debit customer for special processing. If available, the conditions are applied on the debit side of the payment. |
| Routing and settlement | Routes the payment to a clearing channel (SAINST), which determines the message type (pacs.008SI). TPH enriches the information of the creditor and performs creditor validations. |
| Credit bank condition check | Checks for agreement with the creditor bank for special processing on the payment. If a valid agreement is available, the conditions are applied on the credit side of the payment. |
| Date determination | Calculates the dates used for posting, booking and sending the payment. Considers factors (such as shifts, holidays) to arrive at the dates.   - Value date for interest calculation - Booking date – For booking in ledger - Send date for sending the payment  These dates are configured to current or execution date. |
| Duplicate check | Configures the check on payment amount, currency, transaction reference, beneficiary account, and value date. This is configured according to the bank’s requirements. |
| Filtering | Performs risk filtering when interfaced to a screening engine. TPH is pre-integrated with Temenos FCM solution for risk filtering. This is optional and is a bank-specific requirement that is performed in the site. |
| Fee calculation | Calculates the applicable charges. Charge mode is always set as shared (SHA) for Saudi IPS payments. The *Allowed Charge Options* and *Default Charge Option* fields are set as ‘Pay My Bank Charges Only’ in `PAYMENT.ORDER.PRODUCT` table. |
| FX calculation | Calculates and applies FX rate when customer and payment account currencies are different. The following fields are configured in `PAYMENT.ORDER.PRODUCT` table:  - To enable cross-currency transaction, select ‘YES’ in the *Allow Fx* field - To allows user-defined FX rate, select ‘YES’ in the *Allow Fx Rate field* |
| Balance reservation | Reserves the funds on debit account, which is performed on payment amount with or without charges (based on bank’s requirements).  - If Account Management System (AMS) is Temenos Transact, TPH performs funds reservation in embedded mode - If AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system  Funds reservation depends on the values set in *Reserve with Charges* field in `PP.BALANCE.CHECK.REQUIRED` table.  - If set as N, funds reservation is done on payment amount - If set as Y, funds reservation is done on payment amount with charges |
| Message generation | Generates message as specified below:  - Instruction ID- This is generated in the format: YYYYMMDDCCDDDDSSSSYXRRRZHHMMNNNNNN  The instruction ID is generated when the message is stored in ‘SendersReferenceOutgoing’ of the original CT transaction. - Message Structure – The IPS message is generated with message blocks comprising a Business Application Header (BAH) and the Business Payload. Duplicate payment (indicated in BAH). |
| Waiting for response (SLA) | Waits for payment response (pacs.002) from IPS within SLA time when an outward message is generated and sent out. This can be enabled by selecting ‘Debitonpayconfirmation’ in *Postingmethod* field of `PP.CLEARING` table.    - If a response is not received within SLA time, the system generates and sends a duplicate pacs.008 message. SLA time is defined in *InvestigationTimeOut* field of `PP.CLEARING` table. Other mandatory fields, such as *Investigationretrytime*, *Investigationretrycount* and *Clearinginvestigationmsgtype* (as ‘pacs.008SI’) are also defined. - On timeout, a new record in `EB.QUERIES.ANSWERS` is created, which generates an outward pacs.008 with DUPL indicator. - Online service, PP.AUTO.INVSTMSG.GEN.SERVICE must be running to generate an outward duplicate pacs.008. |
| Error queue | If an error occurs during processing, pacs.002 RJCT is sent out. To know more, refer to [Viewing the Payment Enquiries](Working_with.htm#Viewing_the_Payment_Enquiries). |

## Inward Payment Processing



| Activity | Description |
| --- | --- |
| Payment received from IPS network | Receives an inward payment (pacs.008) from Saudi IPS |
| Acceptance | Validates the format and data according to IPS standard.    - If the validation fails, TPH rejects the message and does not process the inward payment. |
| Map and assign weight | - Maps the inward payment (pacs.008) to TPH neutral format and assigns weights to the payment.  - Checks for duplicate indicator ‘DUPL’ in message header and updates the original transaction audit trail as ‘Duplicate Message Received’ and ignores the message.  TPH uses the API defined in *OriginalPmtIDAPI* field of `PP.MSGMAPPINGPARAMETER` table to identify the original transaction.  - If the original transaction is not found, TPH creates a new transaction and processes it. It also stores the inward message or file details in `PPT.RECEIVEDFILEDETAILS` table. To know more, refer to [Viewing the Received Files or Messages](Working_with.htm#Viewing_the_Received_Files_or_Messages). |
| Debit bank condition check | Checks for an agreement with the debtor participant bank for special processing on the payment. If available, it applies the conditions on the debit side of the payment. Bank conditions influences the processing of the following:  - STP or manual - Statement format - Separate charge booking - Advice generation |
| Product determination | Checks the inward payment against a configured payment product to find a match. If a match is not found, it rejects the payment. Payment products influence the processing of the following:  - Client-specific conditions - Fees - Filtering |
| Credit party validation | Identifies the credit party from the inward payment and performs the following validations:  - Credit account is active - No posting restrictions - Beneficiary IBAN - Account is not in quoted currency |
| Credit client agreement check | Checks for an agreement with the credit customer for special processing on the payment. If available, it applies the conditions on the credit side of the payment. |
| Date calculation | Receives payments with value date as current business date or future date. Both payments are processed as STP. For future date payment, the exposure date is set to value date. To know more, refer to [Inward Future Dated Payment](Configuration.htm#Inward_Future_Dated_Payment) section. |
| Duplicate check | Performs the check on payments received from IPS for the configured set of payment attributes, such as payment mount, currency, and transaction reference. This is configured in `EB.DUPLICATE.TYPE` table. This is configured as per bank’s requirement. |
| Filtering | Performs risk filtering of payments when interfaced with a screening engine. TPH is pre-integrated with Temenos FCM solution for risk filtering. It processes response from sanction screening as below:  - Timeout – If there is no response, the transaction is timed out and TPH cancels it on receipt of camt.056 from IPS. It is configured in *MaxInstTimeOut* field in `PP.CHANNEL.CUTOFF` table. - True Hit – If there is a hit, TPH rejects the transaction and generates a status report pacs.002 (RJCT). - Possible Hit – If there is a possible hit, TPH accept without posting (ACWP) response to pacs.002 message. It can be configured by setting *ScreeningResponseAction* field as ‘SendPendingConfirmation’ in `PP.CLEARING` table. - No Hit – TPH continues processing with other components. If all validations are successful, it generates a status report pacs.002 ‘ACTC’.   This is a bank specific requirement and is performed in the site. |
| Fee calculation | Calculates the applicable charges. The default charge condition is ‘SHA’. |
| Posting | Credits the beneficiary account with payment amount by deducting any fees or charges applicable.   - If AMS is Temenos Transact, TPH performs credit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  The accounting entries posted for inward payments are as follows:   - Debit clearing suspense account for IPS - Credit beneficiary account excluding charges - Credit P&L account for charges |
| Message generation | Clearing specific API generates DUPL pacs.002, when it is already generated. TPH generates status report message (pacs.002) with payment status as follows:  - ACTC – Accept for incoming transaction is processed successfully - ACWP – Accept without posting for incoming transaction with a possible hit in sanction screening  - RJCT – Reject for incoming transaction that has failed any validation or timed out in sanction screening |
| Error | If an error occurs during processing, TPH cancels the payment automatically and sends pacs.002 with ‘RJCT’ to IPS. |

## Inward Cancellation Processing

When a response to an outward pacs.008 is sent to the beneficiary bank on time out, IPS sends a cancellation message. On receipt of camt.056, TPH processes the message as follows:



| Activity | Description |
| --- | --- |
| Acceptance | Validates the format and data according to IPS standard.    - If the validation fails, the message is rejected and TPH does not process the inward message. |
| Time out cancel request received from IPS network | Receives inward cancel request (camt.056) from IPS and transforms it to TPH neutral reverse credit format. |
| Identify the original transaction and update the Audit Trail | Identifies and cancels the original transaction, and updates the audit trail.  - If the transaction is not found, it marks the incoming cancellation request as ‘Unmatched’ in `PPT.RECEIVEDFILEDETAILS`. TPH identifies the original transaction by:   - Mapping the Original Instruction Identification tag of camt.056 message to TPH neutral RC ‘OriginalTransactionIdentification’ tag   - Attaching OriginalPmtIDAPI API in `PP.MSGMAPPINGPARAMETER` |
| Message generation | Sends acknowledgement of cancellation to the IPS in the form of pacs.002 (RCVD). When TPH receives a cancel camt.056 message, it generates the message status report pacs.002 with ‘RCVD’. This can be configured by setting the field values in `PP.CLEARING` table as follows:  - *ClearingTransactionType* as ‘CF’ - *Incoming Message Type* as ‘camt.056SI’ - *Outgoing Message Type* as ‘pacs.002’ |

## Inward Response Processing

This section allows to process response from the beneficiary bank and status code, such as Accept (ACTC) or Accept Without Posting (ACWP).

[Beneficiary Bank’s Response for an Outward CT (pacs.008)](#)

A pacs.002 message received with transaction status value as ‘RJCT’ is treated as negative acknowledgement for an outward pacs.008.



| Activity | Description |
| --- | --- |
| Acceptance | Validates the format and data according to IPS standard.  - If the validation fails, TPH rejects the inward message and does not process it. |
| Inward Message Status Report is mapped to TPH neutral format | Receives inward status report (pacs.002) from IPS and maps it to TPH clearing status neutral format. |
| Identify the original transaction and update the Audit Trail | Identifies original transaction based on the original instruction ID. TPH identifies the original transaction by mapping the original instruction identification tag of pacs.002 message to TPH neutral CS ‘OriginalTransactionIdentification’.  - If the original transaction is found, it cancels, releases lock on funds, and updates the audit trail as ‘Cancelled’ - If original transaction is not found, it updates the message status as ‘Unmatched’ in `PPT.RECEIVEDFILEDETAILS` |

[Status Code – Accept (ACTC) or Accept without Posting (ACWP)](#)

A pacs.002 with transaction status value as ‘ACTC’ or ‘ACWP’ is treated as positive acknowledgement (ACK) for an outward transaction or request.



| Activity | Description |
| --- | --- |
| Acceptance | Validates the format and data according to IPS standard.   - If the validation fails, TPH rejects the message and does not process the inward message. |
| Inward message status report mapped to TPH neutral format | Receives an inward status report (pacs.002) from IPS and maps it to TPH clearing status neutral format |
| Identify the original transaction and update the audit trail | Identifies original transaction based on the original instruction ID. TPH identifies the original transaction by mapping the original instruction identification tag of pacs.002 message to TPH neutral CS ‘OriginalTransactionIdentification’.  - If the original transaction is found, it is completed by unlocking the amount and debiting the customer’s account - If the original transaction is not found, it updates the message status as ‘Unmatched’ in `PPT.RECEIVEDFILEDETAILS` |

## Inward Processing of NACK from IPS

When IPS identifies an error in the participant ID or IBAN, it sends an admi.002 to the initiating bank as a reject, which is then processed in TPH.

| Activity | Description |
| --- | --- |
| Acceptance | Validates the format and data according to IPS standard.   - If the validation fails, TPH rejects the message and processes the inward message |
| Inward NACK is mapped to TPH neutral format | Treats inward message as a reject and maps it to a clearing status neutral format. |
| Identify the original transaction and update the Audit Trail | Identifies original transaction based on the original instruction ID available in the additional data tag of the message and maps the instruction identification tag of pacs.008 (embedded) message to TPH neutral CS ‘OriginalBahMessageID’ tag.  - If the original transaction is found, it cancels, releases the lock on funds and updates the status as ‘Cancel’ - If the original transaction is not found, it updates the message as ‘Unmatched’ in `PPT.RECEIVEDFILEDETAILS` |

In this topic

- [Introduction to Saudi Arabia Instant Payments System (SAIPS)](#IntroductiontoSaudiArabiaInstantPaymentsSystemSAIPS)

- [Type of Participants](#TypeofParticipants)
- [Outward Payment Processing](#OutwardPaymentProcessing)
- [Inward Payment Processing](#InwardPaymentProcessing)
- [Inward Cancellation Processing](#InwardCancellationProcessing)
- [Inward Response Processing](#InwardResponseProcessing)
- [Inward Processing of NACK from IPS](#InwardProcessingofNACKfromIPS)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:21:40 PM IST