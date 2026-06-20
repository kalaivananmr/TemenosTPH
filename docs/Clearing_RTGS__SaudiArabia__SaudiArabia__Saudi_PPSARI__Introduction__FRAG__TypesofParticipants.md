# Introduction to Saudi Arabian Riyal Interbank Express (SARIE) - Typesofparticipants

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SaudiArabia/SaudiArabia/Saudi_PPSARI/Introduction.htm#TypesofParticipants

---

# Introduction to Saudi Arabian Riyal Interbank Express (SARIE)

Updated On 08 November 2022 |
 13 Min(s) read

Feedback
Summarize

The Saudi Arabian Riyal Interbank Express (SARIE) is a state-of-the-art payment and settlement system that links all the local banks and allows them to make and settle payments in Saudi Riyals (SR). It is the foundation for Saudi Arabia’s payments system strategy and provides the basis for improved banking products and services. The Saudi Arabian Monetary Authority (SAMA), which is the central bank of Saudi Arabia, has a strong interest in promoting safety and improving efficiency in payment systems as part of its overall concern with financial stability.

## Types of Participants

There are two type of participants in SARIE Single Customer Payment (xSCPAY) payments:

| Participant | Description |
| --- | --- |
| Direct | A participant bank that exchanges payments directly to the clearing and holds a settlement account with clearing. A direct member is identified by value ‘D’ in *Reachability Type* field. |
| Indirect | A member bank that exchanges payments with clearing through a SARIE direct member. Indirect member bank does not hold a settlement account with SAMA. An indirect member is identified by value ‘I’ in *Reachability Type* field. |

Payment can be initiated from a TPH to beneficiary bank who is a direct or indirect participant bank. Information of both the banks can be configured in SARIE version page of `CA.CLEARING.DIRECTORY`.

## Outward Processing of Single Customer Payment (xSCPAY)

This section describes the outward processing of a SARIE customer payment initiated from the Temenos Payments Hub bank to a direct or indirect participant bank of SARIE clearing system.



| Activity | Description |
| --- | --- |
| Manual capture of SARIE payment | - Captures a customer payment request from PO application (PAYMENT.ORDER, SARIE.CTR.INPUT) or Order Entry (OE) page. - Validates whether the following mandatory fields are updated:   - *Debit Account Number*   - *Payment Amount*   - *Payment Currency*   - *Beneficiary IBAN*   - *Account with Institution BIC*  If an error occurs during validation, it is displayed on the page for the user to correct or cancel the payment. If the error requires user intervention to complete the payment capture (such as insufficient balance in debit account), then the user needs to override it to proceed. |
| Account validations | Validates the ordering account for the following:  - Valid Temenos Transact account - Has sufficient balance to cover the transaction - Has no posting restrictions |
| Bank code validations | Validates for the following:  - Beneficiary’s bank BIC (ACWINS) is available - If beneficiary IBAN is available, the country code at position 1, 2 is SA - Beneficiary IBAN is validated for its structure  Validates the IBAN structure in `IN.IBAN.STRUCTURE` table and BIC value in `RD.CENTRAL.BANK.DIR` table. |
| Business validations | Validates for the following:  - Charge option is ‘SHA’. - Maximum Future Value Date needs to be within 14 calendar days. Any value greater than 14 days is rejected. This value is set as 14C in *Allow Future Date* field in `PAYMENT.ORDER.PRODUCT` table. - Generates SCPAY in SARIE standard message format. - Instruction Code is PHOB or TELB.   Purpose of Payment (POP)   - TPH supports Transaction Type Code (Tag 26T) values ‘PAY’ and ‘DIV’. These codes are defined in `PAYMENT.PURPOSE.CODE` table.   - If the value is PAY, the system validates /PAYROLL/ in first 9 characters of Remittance Information (Tag 70)   - If the value is DIV, the system validates /DIVIDEND/ in first 10 characters of Remittance Information (Tag 70) |
| Reachability check | Set the *Skip Reachability* field of `PP.CLEARING` table as N. At payment order level, set the *Reachability Check* field in `PAYMENT.ORDER.PRODUCT` table as BIC. Reachability check criteria is defined in  `CA.CLEARING.DIRECTORY.PARAM` table. To know more, refer to [Reachability in SARIE](Configuration.htm#Reachability_in_SARIE) section. |
| Balance check (not shown in diagram) | Checks whether the debit account has enough funds to process the payment.  - If available, the funds are reserved. - If insufficient, it moves the payment to Manual Fund Authorisation queue and processes the payment on future authorisation. |
| Submission and supervisor approval | Performs the following validations:  - On submission, the payment awaits for Supervisor approval.   - If approved, it is moved for further processing.   - If rejected, it is modified and resubmitted for approval. - Payment is sent to Temenos Payments Hub engine for further processing. |
| Warehouse | Warehouses payments received after the channel cut-off and processes them on the Start of Day (SOD) of the next working day. This is configured in *CutoffTime* or *CutoffShift* field in the `PP.CHANNEL.CUTOFF` table. The Warehouse Indicator field in `PP.BANK.CONDITIONS` table is set as N to disable warehousing at bank condition level. Warehouses the future dated payments in TPH and releases it on the due date for processing. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank-specific requirement and performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (SARIE), which determines the message type (SARIECT). If the system finds that the clearing cut-off time has passed for SARIE, TPH warehouses the payment to release it on the next business day for processing. |
| Dates calculation | Calculates the payment value and booking date, which are configured to current date (similar to execution date) Calculates the payment Credit Value Date (CVD) from the Requested Execution Date (RED) captured in the payment order. If RED is in the future, it processes the payment and sends it to clearing system for processing.  Future date for CVD is defined as 15 in `PP.BOUNDARY.DATE` to place boundary on outward future date payments. |
| Balance reservation | Reserves funds on the debit account, which is performed on payment amount or payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system.  The funds reservation depends on the value set in *Reserve With Charges* field in `PP.BALANCE.CHECK.REQUIRED` table:  - If set as N, then funds reservation is done on payment amount - If set as Y, then funds reservation is done on payment amount with charges |
| Fee calculation | Calculates the applicable charges. The charge mode is set as shared (SHA) for SARIE payments. Charge option is defined in *Allowed Charge Options* and *Default Charge Option* fields (`PAYMENT.ORDER.PRODUCT` table) as ’Pay My Bank Charges Only’ |
| Duplicate check | Configures the check on payment amount, currency, and transaction reference for payments received from an ordering bank. This is configured in the `EB.DUPLICATE.TYPE` table. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (such as Automatic Retry, Reject or Cancel). **Outward Payments**  Entries made before sending MT103 to SARIE   - Debit debtor account (or ordering bank account) - Credit SARIE clearing Nostro account   **Settlement Booking Entry**  When SARIE payments are processed, the clearing Nostro is directly credited or debited. There is no separate settlement processing and hence, no settlement accounting for SARIE payments. |
| SARIE channel validations | Ensures the payment meets the compliance requirements of SARIE. It performs the following validates:  - If payment is initiated from payment order, the ordering party account number needs to be available. - Payment currency and payment charge type need to be in SAR and SHA, respectively. - SARIECT message is validated against MT103 swift validation - When payment purpose is 'PAY' OR '/DIV/', then remittance information needs to start with /PAYROLL/ or /DIVIDEND/, respectively - Maximum length of payment code is three characters - PHOB and TELB instruction codes are mutually exclusive |
| Outward payment generation | Generates SARIECT (MT103) messages and parks the payment in status ‘999’. It updates the following:  - Payment sent file and bulk details - Payment sent message blob files  To know more, refer to [Viewing the Output Payment Files](Working_with.htm#Viewing_the_Output_Payment_Files) section. |
| Error queue | If an error occurs while processing the payment, it moves the payment to the Error queue for the user to repair or cancel the payment. To know more, refer to [Viewing the Outward SARIE SCPAY Payment Transaction](Working_with.htm#Viewing_the_Outward_SARIE_SCPAY_Payment_Transaction) section. |

## Inward Processing of Single Customer Payment Message (xSCPAY)

This section describes the inward processing Single Customer Payment Message (xSCPAY) received from SARIE (of a direct participant bank), destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| SARIE payment received | Receives an inward payment (MT103) from SARIE and transforms to neutral credit transfer format in TPH. Stores the inward message or file details in `PPT.RECEIVEDFILEDETAILS` table.  To know more, refer to [Viewing the Received Files or Messages](Working_with.htm#Viewing_the_Received_Files_or_Messages) section. |
| SARIE format validations | Performs the following SARIE specific validations on the payment:  - Duplicate check (configured in `EB.DUPLICATE.TYPE` table) - IBAN validation (configured in `IN.IBAN.STRUCTURE` table) |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary IBAN unknown - Closed or blocked - Not in currency quoted |
| Dates calculation | Receives SARIE payments with value date as current business date or future date. It processes both the payments as STP, and sets the exposure date of future date payment as CVD. To know more, refer to [Future Dated Payment](Configuration.htm#Future_Dated_Payment) section. |
| Filtering | Performs filtering of payments (if configured). This is a bank-specific requirement and is performed in the site. |
| Fee calculation | Applicable only for customer transfers. Charge bearer is SHA. |
| Duplicate check | Performs duplicate check on payments received from SARIE for the configured set of payment attributes. The criteria is set to payment amount, currency, and transaction reference.  This is configured in `EB.DUPLICATE.TYPE` table. |
| Credit posting | Debits SARIE clearing nostro account and posts the credit to the beneficiary account (59A). |
| Error queue | If an error occurs while processing the SARIE payment, it moves the transaction to the Repair queue for the user to repair or cancel the payment.  To know more, refer to [Viewing the Inward SARIE SCPAY Payment Transaction](Working_with.htm#Viewing_the_Inward_SARIE_SCPAY_Payment_Transaction) section. |

## Inward Processing of SARIE Payment Status Report

Payment status report of outward SARIECT (MT103) messages is received through SARIESR MT298/12 and MT298/35.

[SARIESR (MT298/12)](#)

It is an acceptance message that is treated as positive technical acknowledgement (ACK) for an outward SARIECT (MT103).



| Activity | Description |
| --- | --- |
| Map MT298/12 | Receives an inward message (MT298/12) from SARIE and transforms it to neutral credit transfer status report format in TPH. |
| Update PSM.BLOB | Treats MT298/12 as positive acknowledgement, and updates message content and acknowledgement related fields in PSM.BLOB. |
| Update audit trail | Updates audit trail as payment completed in the original transaction. To know more, refer to [Viewing the Payment Enquiries](Working_with.htm#Viewing_the_Payment_Enquiries) section. |

[SARIESR (MT298/35)](#)

It is a rejection message that is treated as negative technical acknowledgement (NACK) for an outward SARIECT (MT103).



| Activity | Description |
| --- | --- |
| Map MT298/35 | Receives an inward payment (MT298/35) from SARIE and transforms it to neutral credit transfer status report format in TPH. |
| Update PSM.BLOB | Treats MT298/35 as negative acknowledgement and updates the message content and acknowledgement related fields in PSM.BLOB. |
| Update audit trail | Reverses original transaction and updates status as 993. It also, updates the audit trail as payment completed. To know more, refer to [Viewing the Payment Enquiries](Working_with.htm#Viewing_the_Payment_Enquiries) section. |
| Reverse transaction | Generates the reversal accounting entries for the payment. To know more, refer to [Viewing the Payment Enquiries](Working_with.htm#Viewing_the_Payment_Enquiries) section. |

When the value in tag 20 of the incoming MT298 does not match with reference of any valid transaction in the system, the following happens:

- Updates the messages as ’Unmatched’
- Lists the messages in an enquiry for manual action

## Illustrating Model Parameters

To know more on parameter setup for RTGS Payments, refer the [Payment Hub (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm), [Payment Suite (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

The following model products are available under this module:

| S.No | Products | Description |
| --- | --- | --- |
| 1 | SARIE Clearing | This product helps to handle SARIE clearing payments. |