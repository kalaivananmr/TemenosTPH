# Introduction to Tunisia Cheque Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)
    - [Introduction](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)
    - [Configuration](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Configuration.htm)
    - [Working with](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Working with.htm)
    - [Tasks](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Tasks.htm)
    - [Outputs](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Outputs.htm)

Payments

# Introduction to Tunisia Cheque Clearing

Updated On 23 May 2023 |
 20 Min(s) read

Feedback
Summarize

SIBTEL is a central electronic clearing system for Tunisia cheque collection scheme, which allows participant banks to process cheques payments in TND (currency). The below diagrams depict the message flows in Tunisia cheque processing of SIBTEL.






The following message types are used in processing:

- Cheques presented for the first time (30)
- Cheques presented for partial payment (31)
- Cheques presented for payment that follows a Provision Reconstitution Certificate (PRC) (32)
- Cheques represented for payment (33)
- Cheque rejection advance notice (81)
- Non-Payment Certificate (NPC) (82)
- PRC (83)
- Papillons (Technical Rejects) (84)

## Processing an Outward Cheque Collection Request

User can capture a cheque collection request transaction from the Teller module. In the Teller page, the user can capture the cheque presentment types that denote whether the cheque is for the following:

- First time (30)
- Partial payment against the NPC received (31)
- Full payment along with interest amount received in PRC (32)
- Representation against a technical reject (33)

If the request is against the NPC or PRC, the user needs to capture the NPC date and reference, provisional or interest amount from the page. Once the transaction is authorised from the Teller module, the CHEQUE.COLLECTION application in Temenos Transact is updated with the cheque status. The payment details are sent to TPH by invoking an API. Temenos Payment Hub (TPH) creates a transaction record in status ‘4’ and the payment is picked up by a medium weight service for further processing as Straight-Through Processing (STP). As the accounting entries are in Teller module, TPH determines the following:

- Debit and credit party (mapped from Cheque Collection application)
- Clearing channel
- Settlement booking

If the payment is processed without any errors, it parks the payment in 706 status to be picked up by the clearing settlement service. The outgoing cheque presentation or representation is sent to clearing according to the clearing frequency configured in the system, SIBTEL specific naming convention and format. There is a limit to the maximum number of transactions sent in a file to clearing, based on the frequency time file sent to clearing. If the file is sent to the clearing in the:

- First frequency (12:00 PM), there is no limit on the maximum number of transactions sent in a single file.

- Second frequency (12:00 PM to 01:00 PM), the maximum number of transactions in a single file can be 1000.
- Third frequency (01:00 PM to 02:00 PM), the maximum number of transactions in a single file can be 500.

The clearing follows post-settle indirect accounting. Hence, the following accountings are generated in the Teller module when presentation file is sent to the clearing:

- Debit cheque collection clearing suspense account (with the full amount of cheques)
- Credit collection suspense account

On settlement date, it generates the following accountings:

- Credit customer account (with the adjusted amount of rejects received from the clearing)
- Debit collection suspense account

On the settlement date after the reject cut-off (by adjusting the amount of the rejects received in TPH), it generates the settlement entries:

- Debit clearing nostro account
- Credit cheque collection clearing suspense account



| Activity | Description |
| --- | --- |
| Cheque collection request | Captures cheque collection request from the Teller page, where the user can enter the details of cheque along with presentation type (30,31,32,33). The country-specific team handles the capturing of cheque data in Teller page, and mapping of that data in TPH. Payment Order (POR) table objects is also handled by the country layer solution. |
| Credit account validation | Checks whether the credit account is a valid Temenos Transact account and does not have any posting restriction. |
| Reachability check | Validates whether the debtor bank code is reachable through the Tunisia cheque clearing in the Teller page. |
| Routing | Routes the payment to Tunisia cheque clearing based on the routing rule maintained in TPH. |
| SIBTEL cut-off check | Checks the cut-off for sending the outgoing presentation file to SIBTEL. To know more, refer to [Clearing Cut-Off](Configuration.htm#Clearing_Cut-Off). |
| Dates calculation | Calculates the dates for the cheque collection transaction as below:  - *Credit value date* – D (Date on the file is presented to the clearing) - *Day funds are available* – D |
| Duplicate check | Performs duplicate check for outgoing cheque collection transaction based on the various criteria, such as bank, branch, presentation type, cheque number and credit value date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement and is performed in site. |
| Fees calculation | Charges processing fees from the creditor. It can also waive the fees from the Teller while capturing the cheque collection request. |
| Posting | Follows indirect post-settle accounting for cheque processing. To know more, refer to [Clearing Suspense Account](Configuration.htm#Clearing_Suspense_Account). |
| Update cheque collection module | Updates the cheque status in Cheque Collection module to set the cheque status as ‘Deposited’. |
| Generate and send outward file to clearing | Generates Tunisia cheque clearing files (for statuses 30, 31, 32, and 33) by bulking all cheque collection requests according to the presentation type (30, 31, 32, and 33). The file submission to the clearing happens at a pre-defined clearing schedule. |
| Error queue | If an errors occurs during processing, it moves the cheque collection transaction to the Repair queue for manual intervention. Validation errors can be due to failure of any channel level validations in TPH. To know more, refer to [Viewing the CRS Report](Working with.htm#Viewing_the_CRS_Report). |

The Country Layer Solution team handles the creation of local fields, cut-off and reachability check in Teller page. The team also handles indirect accounting configuration on the customer account.

## Receiving and Processing an Inward Reject File

The system can receive NPC (82) reject file for the outgoing presentation (30) when there are errors (such as apposition for theft) on the drawer’s account. As it is a final reject for the cheque payment, it completes the processing of transaction and marks the cheque as ‘Returned’ in the system. It does not allow further representation of the same cheque.

If the system receives Papillons (Technical Reject) 84 reject message for the outgoing presentation (30), it indicates some technical error in the cheque file sent to the drawer’s bank. The cheque representation is based on the reason code received in the message. If the cheque is representable, the user captures a new transaction by correcting the errors. The representation file (33) is generated from the system and sent to the clearing.

If the system receives reject file (81 ‘Cheque rejection advance notice’) for the outgoing presentation (30), then ‘No Funds’ or ‘Partial Funds’ is available in the drawer’s account for the cheque amount.

- If the user doesn’t deposit the required funds for the cheque in the account, the system receives the Final Reject (82) for the cheque presentation on the settlement date.
- If the user deposits the funds between D and D+4, the ordering bank does not receive any message, and the funds are credited to the customer on D+4.

If the payee wants to claim for the partial funds, they can create a new transaction with presentation type as ‘31’ and provide the cheque amount as the partial funds available on the customer’s account. The drawer’s bank debits the customer for the partial funds on receipt of 31 and tries for the remaining funds (for the next 3 months). If the user deposits the funds within the next 3 months, the drawer’s bank sends PRC (83) for the cheque presented. On receiving the PRC, the system sends the representation file (32) to claim the amount for the cheque.

The inward reject file is mapped to TPH neutral mapping objects and the original transaction is identified based on the cheque number, payer and payee account. If the system cannot identify the original transaction for the inward reject, it moves the transaction to the Repair queue. The user can modify the reject transaction from the queue by correcting the error in the transaction. At the end of the processing of the inward reject, it generates the following reversal entries:

- Credit cheque collection clearing suspense account
- Debit collection suspense account

The settlement entries amount is adjusted for the inward reject and the net amount is used for settlement.



| Activity | Description |
| --- | --- |
| Receive the reject file | Receives and maps the reject cheque processing file. The original transaction is identified based on below criteria:  - *Cheque number* - *Payee account* - *Payer account*  It marks the original transaction as ‘Returned’. |
| Reverse the settlement entries | Adjusts settlement entries for the inward reject (as clearing follows post-settle indirect clearing) and generates a net settlement entry booking after the reject cut-off on settlement date. To know more, refer to [Return Code](Configuration.htm#Return_Code). |
| Identify the original transaction | Identifies the original transaction with the transaction reference and updates the status of the transaction as 998 (Completed with Return). If the transactions do not match, the user needs to handle it manually. |
| Update the cheque collection | Updates the cheque collection status as ‘Returned’. Data received in the incoming rejects (such as ‘NPC Date’, ‘NPC No’, ‘Provisional Amount’ and ‘Interest Amount’) is also updated to the original transaction along with the reason code received. |

The Country Layered Solution team handles the processing of inward 81, 82 (followed by 81 on D+4) and 83.

## Receiving and Processing an Inward Cheque File (Presentation or Representation)

The cheque presentation file (30) received from the SIBTEL clearing is mapped to TPH neutral mapping objects. It performs the standard business validations and processes the transaction as STP. At the end of the processing, it generates the customer side bookings and marks the transaction status as ‘999’. The bookings are generated as:

- Debit customer account

- Credit cheque clearing suspense account

The settlement entries for nostro bookings are generated on settlement date after the reject cut-off (09:00 PM) on running the settlement service.

- Debit cheque clearing suspense account
- Credit clearing nostro account

Based on the state of the transaction, the system can also receive (31, 32, 33) representation file from the clearing. The representation file (33) is received against the Papillon message sent earlier to the clearing (84). The processing of the representation file (33) is similar to representation file (30).



| Activity | Description |
| --- | --- |
| Message acceptance | Validates and processes the received files. As a product solution, the system handles the processing of presentation file 30 and 33. The Country Layer Solution handles the processing of representation file 31 and 32. |
| Message mapping | Debulks the Tunisia cheque clearing file, maps the file, and creates the cheque clearing transaction. |
| Debit account validation | Validates the debit account for the following:  - Valid Temenos Transact or DDA account - Active - Does not have posting restriction |
| Cheque number validation | Validates cheque details against cheque register in DDA system or Temenos Transact. If the cheque status is ‘Issued’, it processes the payment further. If the status is already ‘Returned’, a warning indicates the user for overriding it and going ahead with the represented cheque. |
| Balance check | Checks whether sufficient funds are available in the debtor’s account (before posting an inward cheque).  - If funds are available, it performs fund reservation. - If funds are not available, it moves the transaction to status ‘49’ (Waiting - Balance Check DDA Approval).  The Country Layer Solution team handles the rest of the processing of that cheque transaction. |
| Dates calculation | Calculates the debit value date according to the configuration in TPH. To know more, refer to [Settlement Booking Indicator](Configuration.htm#Settlement_Booking_Indicator). |
| Duplicate check | Performs duplicate check on cheque clearing transaction based on the below attributes (if configured):  - *Cheque number* - *Payer account* - *Payee account* |
| Filtering | Performs payments filtering, when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. |
| Charge calculation | Charges fee to the customer, based on the configured Fee product. It applies the calculated fee on the customer’s account during posting. |
| Posting | Generates the settlement entries after the reject cut-off on the settlement date, as the clearing follows post-settle accounting. The customer side accountings are generated after processing the inward cheque. To know more, refer to [Clearing Suspense Account](Configuration.htm#Clearing_Suspense_Account). Auto posting of settlement entries is supported only with PH license. |
| Update cheque status | Updates the cheque status in Temenos Transact cheque register as ‘Cleared’. |
| Repair | Routes cheque collection transactions (that have validation errors) to the Repair queue for manual or automatic action (based on configuration). To know more, refer to [Auto-Reject of Inward Cheques](Configuration.htm#Auto-Reject_of_Inward_Cheques) and [Return Code](Configuration.htm#Return_Code). |

The Country Layered Solution team handles the processing of the representation file (31 and 32). It is performed according to partial or full and interest fund received in the corresponding message.

## Generating an Outward Reject for Inward Cheque Transaction

If any business validation fails for the inward cheque transaction, it moves the record to repair status (235). User can do any of the following in the Repair queue:

- Process the transaction by correcting the error occurred during processing
- Reject the transaction by giving an appropriate reason code for the transaction

The system identifies the appropriate reject file code (82 or 84) for the transaction based on the reason code entered by the user. The reject file (82 or 84) is sent to SIBTEL in an acceptable format and naming convention.

- If sufficient funds are not available in the drawer’s account, it moves the transaction to status ‘49’ (Waiting – Balance Check DDA Approval).
- If funds are not available till the settlement date, the system generates the Rejection Advance Notice (81) in SIBTEL acceptable format and naming convention.
- If funds are available in the customer’s account between D and D+4, the system debits the customer account with the cheque amount and does not generate any outgoing transactions.
- If the funds are not available till the settlement date, the system generates Non-Payment Certificate (82) in SIBTEL acceptable format and naming convention, and sends it to clearing.

After sending NPC (82), the payee can claim the partial funds and send a presentation file (31) to claim it. On reception of the presentation file 31, the drawer’s bank debits the customer for the partial funds and tries for the remaining funds for the next 3 months. If the user deposits the rest of the funds in the next 3 months, the system generates the PRC (83) for the cheque presented. If the system receives the presentation file (32) in response of PRC, the system debits the customer for the funds (on receipt of 32) and completes the cheque processing.

The outgoing reject file is generated according to the channel cut-off and frequency configuration in the format acceptable to SIBTEL clearing. It generates the following accountings in the outgoing reject transaction flow against:

- Original Transaction
  - Debit cheque returns suspense account
  - Credit cheque clearing suspense account

- Reject Transaction
  - Debit cheque clearing suspense account
  - Credit cheque returns suspense account

The settlement entries for inward cheque amount is adjusted with the amount of the reject transaction, and the net amount is used for settlement at the end of reject cut-off.



| Activity | Description |
| --- | --- |
| Reject initiation | - If automatic reject is configured in the system, it generates a reject message automatically based on the error and configures a reason code. - If automatic reject is not configured in the system, it moves the transaction to the Repair queue, and the user needs to manually reject the transaction (by selecting the appropriate reason code for the transaction). As part of product solution, system generates reject files 82 and 84. This is followed by reject files 81 and 83, which the Country Layer Solution team handles.  To know more, refer to [Auto-Reject of Inward Cheques](Configuration.htm#Auto-Reject_of_Inward_Cheques). |
| Reject type identification | If the automatic reject is configured in the system, it identifies the reason code applicable for the outgoing reject based on the error code configured. The system identifies the reject type (82 or 84) based on the reason code. |
| Clearing cut-off time check | Validates whether the cheque clearing cut-off time has passed. If yes, it moves the settlement date to the next business date and sends the reject on the next day. To know more, refer to [Clearing Cut-Off](Configuration.htm#Clearing_Cut-Off). |
| Fee calculation | Collects fee from the customer for unsuccessful processing of cheque clearing transaction. It calculates all fees based on the Fee products configured in TPH. |
| Posting | As the clearing follows post-settle indirect clearing, it adjusts the settlement entries for the outward reject, and generates a net settlement entry booking after the reject cut-off on settlement date. To know more, refer to [Clearing Suspense Account](Configuration.htm#Clearing_Suspense_Account). |
| Mark original payment as returned | Marks the original cheque clearing transaction as ‘Returned’ and updates the cheque status of cheque register in Temenos Transact as ‘Returned’. The Country Layer Solution team handles the marking of specific cheque statuses as ‘Partially Paid’ or ‘Partially Returned’. |
| Generate reject message | Generates an outward reject file and forwards it to clearing by bulking all the processed reject transactions. The file is then sent to the clearing at a pre-defined clearing schedule (clearing frequency configuration). It marks the reject transaction status as ‘Completed’. |

The Country Layered Solution team handles the generation and processing of Reject file (81, 83, 82) (followed by 81).

## Receiving and Processing Inward CRS Report Files

CRS file (received from the clearing) has details of all transactions exchanged between the clearing and bank. The inward CRS file is mapped to TPH neutral mapping objects using an inquiry that helps the user view the data received in the file in report format. To know more, refer to [Viewing the CRS Report](Working with.htm#Viewing_the_CRS_Report) for details on the inquiry of CRS report.

To know more about the following features, refer to the Country Layer Solution.

- Cheque related information captured from the Teller page
- Inward 81 and 82 processing
- Inward 82 (followed by 81 on D+4) processing
- Outward 81 generation and processing
- Outward 82 (on D+4) generation and processing
- Retry and blocking for funds on the payer’s account
- Outward 83 generation and processing
- Inward 31 and 32 processing

In this topic

- [Introduction to Tunisia Cheque Clearing](#IntroductiontoTunisiaChequeClearing)

- [Processing an Outward Cheque Collection Request](#ProcessinganOutwardChequeCollectionRequest)
- [Receiving and Processing an Inward Reject File](#ReceivingandProcessinganInwardRejectFile)
- [Receiving and Processing an Inward Cheque File (Presentation or Representation)](#ReceivingandProcessinganInwardChequeFilePresentationorRepresentation)
- [Generating an Outward Reject for Inward Cheque Transaction](#GeneratinganOutwardRejectforInwardChequeTransaction)
- [Receiving and Processing Inward CRS Report Files](#ReceivingandProcessingInwardCRSReportFiles)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:34:12 PM IST