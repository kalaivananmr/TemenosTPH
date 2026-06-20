# Introduction to Faster Payment System (UK FPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/UK/UK/UK_Fast_Payments_System_FPS_PPUFPS/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   United Kingdom > [Faster Payment System](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Introduction.htm) > Introduction

- United Kingdom;)
  - [Faster Payment System Faster Payment System](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Introduction.htm)
    - [Introduction](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Introduction.htm)
    - [Configuration](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Configuration.htm)
    - [Working with](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Working_with.htm)
    - [Tasks](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Tasks.htm)
    - [Outputs](../../UK/UK_Fast_Payments_System_FPS_PPUFPS/Outputs.htm)
  - [CHAPS CHAPS](../../UK/UK_CHAPS_Clearing_PPCHAP/Introduction.htm)
  - [BACS BACS](../../UK/UK_BACS_Clearing_PPBACS/Introduction.htm)
  - CHAPS in ISO20022 (MX);)

Payments

# Introduction to Faster Payment System (UK FPS)

Updated On 22 March 2025 |
 22 Min(s) read

Feedback
Summarize

UK Faster Payment System (UK FPS or FPS), is a 24x7 instant payment processing system that processes domestic payments within the UK. UK FPS processes the following:

- Credit transfers (It operates only in GBP currency)
- Retail and corporate payments with a maximum transaction limit of 250,000 GBP

The beneficiary bank makes the credit available for the beneficiary in real time or near-real time. The SLAs for this vary from few seconds to hours depending on the participation level of the receiving bank in UK FPS scheme. FPS operates in ISO8583 format (a text based fixed length format), that is mainly used for processing the card transactions. Starting from 2022, UK FPS Scheme will offer banks to exchange messages in ISO20022, while in the interim, banks (that cannot send payments in ISO8583) can employ a FPS gateway that converts ISO20022 to or from 8583 format. Bank to bank settlement can be done in the domestic RTGS system with three settlement cycles in a business day. Settlement is done on deferred multilateral net basis.

[System Context](#)

The diagram below shows the system implementation context.



|  |  |
| --- | --- |
| Instant Payments System | Temenos Payment System that allows the user to capture FPS instant payments (Single Immediate Payment and Standing Orders Payment), and process inward and outward payments.  - Comprises two business modules:  - `PAYMENT.ORDER (PO)` application - Temenos Payment Hub (TPH) |
| ESB | Interface gateway of Temenos Payment System to interact with FPS gateways.  - Interacts with ESB using internal Temenos format. - ESB interfaces with FPS clearing gateways. - Temenos Payment Solution is pre-integrated with IBM’s ESB software (IIB). - Adapts workflow for other ESBs as part of project implementation. |
| FPS CI | Instant payments clearing system of UK. |
| FPS Gateway | Bank’s gateway to FPS CI system converts iso20022 messages to iso8583 and vice versa. |
| Bank Host Systems | Bank systems that interface with Temenos Payments Hub System to supplement payments processing. |
| Temenos Payment Solution | Comprises the following modules:  - `PAYMENT.ORDER``(PO)`application – Bank user can manually capture the payment requests. - `STANDING.ORDER``(STO)` application – Bank user can manually capture the standing instructions. - TPH – Payment processing engine. |

|  |  |
| --- | --- |
| Instant Payments System | Temenos Payment System that allows the user to capture FPS instant payments (Single Immediate Payment and Standing Orders Payment), and process inward and outward payments.  - Comprises two business modules:  - `PAYMENT.ORDER (PO)` application - Temenos Payment Hub (TPH) |
| ESB | Interface gateway of Temenos Payment System to interact with FPS gateways.  - Interacts with ESB using internal Temenos format. - ESB interfaces with FPS clearing gateways. - Temenos Payment Solution is pre-integrated with IBM’s ESB software (IIB). - Adapts workflow for other ESBs as part of project implementation. |
| FPS CI | Instant payments clearing system of UK. |
| FPS Gateway | Bank’s gateway to FPS CI system converts iso20022 messages to iso8583 and vice versa. |
| Bank Host Systems | Bank systems that interface with Temenos Payments Hub System to supplement payments processing. |
| Temenos Payment Solution | Comprises the following modules:  - `PAYMENT.ORDER` `(PO)`application – Bank user can manually capture the payment requests. - `STANDING.ORDER` `(STO)` application – Bank user can manually capture the standing instructions. - TPH – Payment processing engine. |

[Types of Fast Payments System](#)

FPS handles the following payments:

| Payment System | Description |
| --- | --- |
| Single Immediate Payment (SIP) | Credits instant payment to the beneficiary in near-real time. |
| Standing Orders Payments (SOP) | Initiates the following:  - Single payments (automatically) based on a previously captured standing instruction. - SOPs in the start of business day, and credits the beneficiary in near-real time or same day. |
| Forward Date Payments (FDP) | Captures single payments by the submitting member bank as a future dated payment.  - Warehouses the payment until the value date and releases to the CI (automatically), to credit it in near-real time to the beneficiary. - Releases FDP at the start of day of the value date. - In addition, the banks can submit FDP intra-day (one or more times on the value date). |
| Bulk Payments | Batch payments sent by members (FIM) or corporates (DCA).  - Gateway module splits the batches into single transactions before submitting to FPS CI. - Clears the payment in near-real time or same day. - TPH supports receiving of DCA payments only. |

[Types of UK FPS Messages](#)

Temenos Payments Hub Solution supports the following UK FPS message types:

| Message | Description |
| --- | --- |
| pacs.008 | This message type is used for two reasons:  Payment Request  - Submitting bank sends pacs.008 to FPS CI. - FPS CI sends this message to the receiving bank.  Scheme Return  - FPS CI sends pacs.008 to the sending bank (debtor’s bank).  This is sent when the beneficiary bank returns an SOP or FDP request. - Scheme return pacs.008 has the FPID of the returned original request. |
| pacs.002 | - Payment response is also known as Payment Status Report (PSR) - The sending bank receives pacs.002 from FPS CI. The receiving bank sends this as a response to the payment request. |
| pacs.007 | - Payment reversal is also known as FPS scheme reversal. - FPS CI sends pacs.007 to the receiving bank. |

[Manual Capture of FPS](#)

Temenos Payment Solution offers a payment capture page for the following FPS types:

- SIP
- FDP
- SOP

[Account Redirection](#)

UK FPS offers a special service known as Account Switching Service (CASS), which allows the banks to register account redirection information within the CI. If redirection is configured for an FPS (received for an account):

- CI replaces the account with the redirect account information and forwards the payment to the beneficiary bank.

The beneficiary bank is unaware of the account redirection available in the payment, and processes it as a regular inward payment.

- CI advices the redirected account information to the originating bank in PSR. The originating bank updates its payment information with the redirected beneficiary account details.

The following deployment options are available when the TPH supports receiving account redirection:

|  |  |
| --- | --- |
| FPS receiving bank (beneficiary bank) | TPH processes the payment using redirected account information. |
| FPS sending bank (originator’s bank) | TPH accepts the redirected account information and stores them for reference. |

[UK FPS Qualifier Codes](#)

The bank may not credit the beneficiary immediately on the receipt of an inward payment in FPS scheme. This depends on the following:

- Own technical infrastructure
- Arrangements with the originating bank
- Account with institution bank

For FPS scheme, the beneficiary bank instructs the originating bank about the time frame for credit availability. This is done using qualifier codes in PSR with the following options:

| Qualifier Code | Qualifier Description |
| --- | --- |
| 0000 | Credit is provided instantly |
| 0081 | Credit is provided on the same day |
| 0082 | Credit is provided on the next day |
| 0083 | Credit date is undeterminable |

TPH offers instant credit availability, when it operates with Temenos Core Banking (Transact) as an Account Management System (AMS) or an external core banking system.

1. If the system is unavailable to perform real time postings (due to maintenance), TPH needs to be intimated.
2. If intimated, TPH continues to accept FPS but responds with a ‘Delayed Credits’ qualifier code.

TPH advices delayed credit availability by using appropriate qualifier code as given below:

| Qualifier Code | Qualifier Description |
| --- | --- |
| 0000 (Accepted without qualification) | Immediate credit |
| 0083 | DDA system is down and the credit is available in future (but at an unspecified time and date). |

[Prioritisation for UK FPS](#)

TPH can change the categorisation at project implementation level, based on the bank’s requirements. It involves:

- Prioritisation of SIP during its processing (real time payments).
- Processing of SOP and FDP with lower priority (near-real time payments).

[Clearing Cut-off](#)

FPS has the following cut-off definitions:

| Definition | Description |
| --- | --- |
| FPS SIP | No cut-off is defined. |
| FPS SOP | No cut-off is defined.   FPS recommends that bulk of the Standing Orders is submitted before 6 AM. FPS is configured as a clearing that supports 24/7 operations. Therefore, no cut-off validations are required (if configured). |

[Scheme Reversals](#)

CI sends scheme reversals to the receiving bank when PSR is not received for a previously sent payment request. Scheme reversals are applicable only for synchronous mode of processing. CI requires a response to a payment request within the predefined time. CI initiates scheme reversal when the session times out waiting for a PSR. On receipt of scheme reversal, the receiving bank needs to do the following:

1. Mark the original payment as reversed.
2. Undo any bookings previously made against the original payment.
3. Return a positive acknowledgement.

If the original payment is not found, the scheme reversal is recorded with no specific processing.

Scheme reversals are sent as pacs.007 message.

[Scheme Return](#)

Scheme return has return code instructed in PSR by the beneficiary bank with no associated SLAs in CI. CI generates and:

- Sends scheme return to the submitting bank (debtor bank), when the beneficiary bank rejects the previously processed SOP or FDP. The submitting bank then credits the payment initiator with the value of the return payment.
- Returns the scheme as a new payment by its own right as original payment is already settled in CI by the sending bank. The sending bank processes the payment independent of original payment, and always returns acceptance to CI (that is, scheme return payment cannot be returned).

Scheme return refers to the original payment request as remittance information (for information purpose).

[Resend Payments to FPS CI](#)

Sometimes originating bank may want to resend a payment, if status response is not received in time for the original payment message.

- When the originating bank sends a credit transfer payment, it usually receives a response (as a status message) from clearing in real time.
- If the originating bank does not receive a status response from clearing, it resends the payment message after waiting for certain time (configured in TPH). The system does not create another payment for this purpose.
- When no response is received from clearing for a payment, the payment is resent to FPS at pre-defined intervals (in seconds) based on the configuration.

[Receive Repeat Messages from FPS CI](#)

If the clearing does not receive status response from the beneficiary bank, it sends a repeat payment message to the bank. The repeat payment message received from clearing, is identified as a ‘repeat’ by TPH. This can happen if:

- PSR sent by the beneficiary bank does not reach the clearing, due to some technical issues.
- The beneficiary bank did not send the PSR to clearing, due to some technical issues.

An immediate clearing status message is sent depending on whether the original payment is successful or failed.

- Audit trail of the original payment is updated with the details of the repeat response sent to clearing.
- If original payment is not found, then the repeat payment is processed as a new payment (regular processing of inward FPS).

[FPS CI Status Change Message](#)

When there is a change, CI sends status update messages to all FPS participants. The possible statuses are:

- Active
- Suspended

Status updates are received as Unsolicited Message (USM). USM is an 8583 formatted message. This is converted to Temenos native message (OFSML) in the bank’s gateway. To know more, refer to see [Interfaces](../../Payment_Initiation_(PI)/Interfaces_and_Message_Standards/Introduction.htm). `PO` application or TPH validates the service status while a payment is manually initiated. If clearing status is ‘Suspended’, TPH:

1. Triggers an error disallowing initiation.
2. Processes outgoing or redirected UK FPS in STP mode.
3. Validates the payment during payment processing and parks the payment in Repair queue.

The user can change the service status from TPH.

[DCA Payments](#)

DCA payments are received as individual payments (pacs.008) from FPS CI. TPH accepts and processes these regular incoming payments with exception that FPS type is recorded as 50.

[Outward Processing of UK FPS](#)

Outward processing of SIP, FDP and SOP involves two payment modules.

- `PO` application
- TPH

The flowchart given below shows the sequence of processing activities involved in the payment.



| Activity | Description |
| --- | --- |
| Manual capture of SIP | - Captures a FPS SIP from `PO` application. - Validates mandatory and non-mandatory fields on submission and displays an error (if any). |
| Automatic initiation of SOP | Temenos Transact SOD process automatically initiates a SOP on the processing date. `PO` application receives SO for further processing and distribution to FPS CI. |
| **Business validations** – The system performs the following business validations on the payment. If any of the validations fail, SIP are parked in Repair queue for user action. SOP are cancelled automatically. | |
| Account validations | - Validates debit account, if it is present in Temenos Transact. - Validates the IBAN structure, if the user enters debtor or beneficiary IBAN. - The system fetches debtor IBAN from Temenos Transact database, if not present in the instructions. |
| Bank code validations | - Validates the BIC, if the user enters the creditor bank BIC. - Derives the BIC based on IBAN (if IBAN is available), if the user does not enter the creditor bank BIC. |
| CI service status | Validates if the FPS CI service status is ‘Suspended’. |
| Duplicate checks | - Duplicate checks are not performed during initiation (as this is not mandated by scheme rules). - The bank can configure as per specific requirements. |
| Transaction limit | Validates the FPS transaction limit against payment amount. |
| Reachability check | Validates if the beneficiary bank (sort code) is reachable directly or indirectly. |
| Payment simulation applicable only when:  - A payment is manually captured using `PO` application or - Customer facing channels interact with `PO` application.  During the simulation, the system calculates the following:  - Applicable charges - Value date - Exchange rate (if FX involved)  The user submits or abandons the payment based on the above. Simulation can be enabled when `PO` application is operating with TPH as payment system. `PO` application can be configured to perform basic simulation when installed with a non-Temenos payment system. This is limited to configuration of charges and value date calculations. Clearing or customer specific validations are not performed by `PO` application. Simulation involves the following steps: | |
| Account restrictions | The system validates the following:  - Posting restrictions on debit account - Posting restrictions on credit account (if the account is in the same bank)  If the account has restrictions, cancel the payment order (if manually captured) or send negative PSR. |
| Cut-off check | FPS is 24x7 system and operates with no clearing cut-off. The payment is therefore not validated for cut-offs. |
| Dates calculation | The following fields are assigned the same date as the current system date.  - *Acceptance Date Time* - *Execution Date* - *Credit Value Date* - *Debit Date* |
| Charge calculation | The system calculates all the applicable charges for the payment (as configured). |
| Balance check | The system performs balance check on debtor account for total value of payment amount and charges. If account does not have sufficient balance, then the system cancels the payment order. |
| Once the user submits the payment post simulation, the payment awaits Supervisor approval.  - If approved, the payment is moved for further processing. - If rejected, the payment can be modified and resubmitted for approval.   SOP are automated payments and are not subject to simulation. | |
| Fraud check | If configured, the system invokes fraud check. A fraud check request is sent to Fraud Check Engine and the status of the payment is updated when fraud check response is received. Payment may be set to Cancelled, or Continue Processing based on the configuration. |
| Send payment to payment system | Payment order is sent to payment system for execution.  - If the payment system is TPH, then the transfer is embedded between `PO` application and TPH. - If the payment system is third party (not Temenos), then an payment initiation message (pain.001) is generated by `PO` application.  The payment system acknowledges the receipt of the payment initiation message in both the cases and payment is in ‘Placed’ status in `PO` application. |
| Time stamping the payment | FPS does not have timestamp as SLA is not validated (based on payment initiation time point). However, payments are still timestamped in TPH as it is used in future developments for generating duplicate payment requests in case of exception scenarios. FPS runs an internal counter from the time it receives the payment from the originating bank to the time it sends a PSR to the originating bank. However, this is not based on any timestamp information in the payment file. |
| Filtering | TPH performs filtering of payments, if configured.   This is a bank specific requirement and handled during implementation. |
| Routing | The payment is routed to UK FPS clearing channel, which is configured to route to FPS CI (by using IIB). Clearing channel determines the message type (FPS pacs.008). |
| Charge calculation | TPH calculates the charges applicable for the processed payment. Calculated charges are displayed as debit side charges (against the payment) after this activity. The charges calculated are same as the calculations done during simulation.   If charge configuration is changed after the simulation activity, then the calculation is different. All fees including FPS transaction fees (if any) are set as per bank specific requirements during implementation. |
| Funds reservation | This activity reserves funds on the debit account. This is a bank specific requirement to be done during implementation. To reserve funds, configure *Source*, *Account Type* and *Message Type* in `PP.BALANCE.CHECK.REQUIRED` table.  - If AMS is Temenos Transact, then TPH performs funds reservation in embedded mode. - If AMS is external, then it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Debit posting | Debtor’s account is debited with payment amount and any charges are borne by the customer. If posting fails due to insufficient funds, the payment is cancelled.  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, then it generates posting request in a standard XML format and accepts response from the external system. |
| Outward payment generation | IIB generates payment request and it complies to FPS schema defined in ’pacs.008.001.06 FIToFICustomerCreditTransferV06 pain.001’. Payment is parked in ‘Awaiting PSR’ status. |

[Inward Processing of UK FPS](#)

| Activity | Description |
| --- | --- |
| FPS received from CI | TPH receives an inward payment from CI in the following scenarios:  - Processes SIP request and sends a payment response in real time. - Processes SOP request (FPS settled) and sends the response in near-real time or same day.   TPH processes both the payment types using the same workflow. |
| **Business validations** – The following business validations are performed when CI receives a pacs.008. | |
| Duplicate check | Validates if FPS ID is duplicated within the last 7 business days (configurable). FPID is a combination of following fields in payment request.  - *Sending FPS Institution* - *Currency* - *Date Sent* - *Payment Type Code* - *Transaction Reference Number (TRN)*   Message ID or TXID of pacs.008 is not checked for duplicate. Message ID is different from the one sent by the originating bank to FPS CI. |
| Account validation | Validates the beneficiary account:  - Beneficiary sort code or account number unknown - Beneficiary account closed - Beneficiary account stopped - Beneficiary account name does not match with the beneficiary account number (not performed for FPS) - Account is not in the quoted currency |
| Bank code validation | NA |
| Account restrictions | Validates restriction on beneficiary account  - Account does not permit credits |
| Generate PSR (failed) | If any of the business validation fails, the system generates a PSR in FPS pacs.002\*\* format (with response status as failed, and an appropriate FPS error code). |
| Calculate charges | In case of charge code SHA, any applicable charges are calculated and applied on the payment. |
| Beneficiary credit posting | Beneficiary is booked with payment amount minus any applicable charges with value date as instructed in the Interbank Settlement Date. |
| Generate PSR | The system generates a PSR in FPS pacs.002\*\* format with response status as Success, and an appropriate FPS qualifier code. The qualifier code is always set at ‘000’ by TPH for SIP and SOP, indicating that the credit is made to the beneficiary in real time. The solution can be enhanced in future to provide pending confirmations when Core Banking system is down. |

## Illustrating Model Parameters

Read the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guides for information on parameter setup for Faster Payments.

## Illustrating Model Products

PPUFPS module provides the facility to send, receive UK Faster Payments.

In this topic

- [Introduction to Faster Payment System (UK FPS)](#IntroductiontoFasterPaymentSystemUKFPS)

- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Temenos Payment Services](../../Services/Misc/Services.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:34:50 PM IST