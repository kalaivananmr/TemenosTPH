# Introduction to MASAV Clearing - Currencyandfx

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Israel/Israel/MASAV_PPMASV/Introduction.htm#CurrencyandFX

---

# Introduction to MASAV Clearing

Updated On 08 November 2022 |
 12 Min(s) read

Feedback
Summarize

MASAV is an electronic system that settles interbank movements (debit and credit instructions), such as account debiting authorisations (‘standing orders’), salary payments, and tax rebates. It is transferred by the banks and other institutions that are authorised to send direct instructions to the Automatic Clearing House. Banks send the debit and credit instructions to clearing house (MASAV) on every working day. The clearing house clears the payments and sends the feedback file to the bank for confirmation.

## Types of Messages

TPH supports the below message types for MASAV clearing:

| ISO 20022 Message | Description |
| --- | --- |
| MASAV Credit Transfers (MASAVCT) | Originating bank generates it in response to a credit transfer initiation (MASAVCTI). MASAV performs the following:  - Sends back a feedback file for reconciliation - Settles and forwards the payment to the beneficiary bank |
| MASAV Direct Debits (MASAVDD) | Beneficiary bank generates it in response to a direct debit initiation (MASAVDDI). MASAV performs the following:  - Sends back a feedback file for reconciliation   MASAV DD needs to be sent to clearing a day prior to the settlement date.   - Credits the beneficiary on the settlement day |
| MASAV Credit Returns (MASAVRT) | If a MASAVCT cannot be credited, the beneficiary bank generates a MASAVRT as a return payment. MASAV forwards the MASAVRT to the originating bank. |
| MASAV Direct Debit Returns (MASAVRF) | If a MASAVDD cannot be debited, the debtor bank generates a MASAVRF as a return payment. MASAV forwards the MASAVRF to the creditor bank. |

## Architectural Diagram of MASAV Clearing

The below diagram shows the supporting solutions for handling loan disbursements and repayments in Temenos Payment Hub (TPH).

- Direct credit is the efficient method to perform loan disbursement.
- Similarly, loan repayment is done through direct debits (also known as debit requests).

/Introduction to MASAV Clearing.png)

The following terms are used in MASAV payments:

| Terms | Description |
| --- | --- |
| Bank’s Straight-Through Processing (STP) channels | TPH’s own bank electronic channels or aggregators |
| Ordering bank | A bank or company sending payment instructions to be cleared with MASAV |
| Payment order | Front-end TPH module to manually capture MASAV payments or receive payment instructions from customer channels or AA module |
| Payment engine | TPH system processes the payments and manually captures the MASAV payments from the back office |
| IIB | TPH interacts with the MASAV system by using middleware |
| MASAV | ISRAEL clearing |
| AML | Bank’s Anti-Money Laundering |
| Temenos Transact or external DDA | Temenos Transact |

## Participants

MASAV clearing can only support direct participation. Hence, TPH supports to configure the banks as direct participants.

## Currency and FX

MASAV handles only single currency Israeli Shekel.

## Cut-Off Time

The user can configure cut-off time by using the `CHANNEL.CUTOFF` table in the TPH to meet the needs of MASAV clearing framework business.

|  | Weekdays | Saturday Night or Night Following a Holiday |
| --- | --- | --- |
| Session 1 | 22:30 | 22:30 |
| Session 2 | 01:00 (the following day) | 23:00 |

## Manual Actions (Repair)

The manual actions of the originating and beneficiary banks are as follows:

| Bank | Description |
| --- | --- |
| Originating | TPH sends the payment to the Repair queue for all the inward returns received for the credit transfer (later, the bank handles this manually). |
| Beneficiary | Returns received for Direct Debits (DD) are handled in STP. However, if the original transactions are not found or found with error, it is manually handled by the bank. |

## Holidays and Time Zone Requirements

According to the standard TPH functionality, the country or Israel-specific holidays can be defined in the core `HOLIDAY` table (in Temenos Transact) and clearing holidays in the `PP.CLEARING.NONWORKINGDAY` table.

## Warehouse

This can be skipped as the need for warehousing is not mentioned. Further, TPH cannot receive future-dated payments, therefore, warehousing is not required.

## Transaction Limits (Value and Volume)

This is not applicable as MASAV handles both retail and large-value payments.

## Banks Directory and Reachability Check

TPH does not perform channel reachability check while processing the payment, as it is not mandated.

Accounting (Postings)

| Method | Type of Account |
| --- | --- |
| Outward CT (entries before the MASAVCT is sent to MASAV) | Debit customer account, Credit MASAV clearing nostro account |
| Outward DD | Debit MASAV clearing nostro account, Credit customer account |

## Distribution to Clearing

This has separate files for debits and credits, which needs to be a single bulk with multiple payments and same charge date. These files have the debits or credits to be sent to MASAV clearing from various institution IDs.

## Payment Cancellation

If an outward payment fails during processing, then it can be cancelled in STP.

## Outward Payment Processing

/Introduction to MASAV Clearing_1.png)

Direct credit is the efficient method to perform loan disbursement (which is paying loan proceeds to the loan borrower). AA framework generates contract based loan disbursements and sends it to TPH on the value date of the payment. Payment Order can capture a payment request and routes it to TPH or an external payment system. It can perform several validations on the payment to ensure the necessary information is passed to the payment system.

## Payment Flows

[Outward Direct Credits](#)

| Activity | Description |
| --- | --- |
| Payment order | Customers can send direct credit request through channels interfaced with `PAYMENT.ORDER` application in TPH. |
| Manual initiation of direct credit requests | Bank users can directly initiate an outward direct credits by using the Order Entry (OE) page |
| System performs the following business validations on direct credits: If the validation fails, it cancels the direct credit request. | |
| Account restrictions | Validates posting restrictions on Debit AccountCancels the payment when an account has restrictions |
| Bank code validations | Validates the sort code of creditor bank, when it is available in the transaction |
| Duplicate checks | Performs duplicate checks on the payment |
| Reachability check | This check is not applicable as MASAV clearing has not mentioned the need for reachability. If required, it can be configured. |
| Warehouse | Does not receive future dated payments, hence, it is not required. |
| Dates calculation | Calculates the processing and send dates, debit and credit value dates based on the settlement shift configuration |
| Channel cut-off | Configures the source MASAV and respective message type |
| Balance check | Performs check on debtor account for total value of payment amount and charges.  If sufficient balance is not available, it cancels the payment. |
| Fraud check | Performs the check (if configured) by sending a request to Fraud Check Engine and updates the status of the payment when the response is received. The payment can be set to Cancelled or Continue Processing based on configuration. |
| Filtering | Performs filtering of payments (if configured), which is a bank-specific requirement that is handled during implementation |
| Routing | Routes the payment to a clearing channel (MASAV), which is configured to route to MASAV clearing |
| Charge calculation | Calculates all the applicable charges for the payment (as configured) |
| Funds reservation | Reserves funds on the debit account This is a bank-specific requirement and is performed during implementation. To reserve funds, the user can configure *Source*, *Account Type* and *Message Type* fields in the `PP.BALANCE.CHECK.REQUIRED` table. |
| Posting | Has the following accounts:  - Debit debtor account (sent from AA to TPH) - Credit MASAV clearing suspense account (sent from outgoing payments to MASAV)   Account entries for settlement transaction are as follows:   - Debit clearing suspense account - Credit clearing Nostro account |

[Process Inward Credit Transfer Returns](#)

TPH can support in receiving the return file, when clearing or receiving bank has rejected the payment. It moves the transaction to repair when the *NONSTPIndicator* field is configured at product determination level. If the user performs the required actions on Repair queue, it rejects the original payment and updates the status as ‘Payment Completed with Return’.

[Outward DD Collection Requests](#)

| Activity | Description |
| --- | --- |
| Automatic initiation of Outward DD Collection | Sends DD Collection request to TPH for processing (by using DD module)Additionally, DD items can be raised toward loans and deposits collections and sent to TPH for processing by using AA module. |
| System performs the following business validations on the DD collection:  If the validation fails, it cancels the DD collection request. | |
| Account validations | Validates whether the debtor IBAN is available within the bank and considers the payment as book payment |
| Account restrictions | Validates posting restrictions on debit account when it is an own account (account within the same bank) If an account has restrictions, it cancels the payment and sends an update to the DD module along with return reason code. |
| Bank code validations | Validates the sort code of the debtor bank, when available in the transaction |
| Duplicate checks | Performs duplicate checks on the payment |
| Reachability check | This check is not applicable as MASAV clearing has not mentioned the need for reachability. If required, validate the sort code of the debtor bank against Extended Industry Sort Code (EISCD) for reachability. |
| Warehouse | Warehousing is not required for MASAV transactions |
| Cut-off check | Sends MASAV file at specified time periods Banks can define or configure their own cut-off to accept DD requests. |
| Dates calculation | Calculates the processing and send dates, debit and credit value dates based on the settlement shift configuration |
| Balance check | Performs check on debtor account for total value of payment amount and charges. If sufficient balance is not available, it cancels the payment. This is applicable only when the debtor account is held within the bank. |
| Fraud check | Performs fraud check (if configured) by sending a request to Fraud Check Engine and updating the status of the payment when the response is received. Payment is set to Cancelled or Continue Processing based on configuration. |
| Filtering | Filters the payments (if configured), which is a bank-specific requirement that is handled during implementation |
| Routing | Routes the payments to a clearing channel (MASAV) |
| Charge calculation | Calculates all the applicable charges for the payment (as configured) MASAV has not defined any clearing specific fees. |
| Funds reservation | Reserves funds on the debit account  - To configure this, enter the required details in *Source*, *Account Type* and *Message Type* fields in the `PP.BALANCE.CHECK.REQUIRED` table.   - This is applicable only for the debtor account that is held within the bank. - This is a bank-specific requirement and is undertaken during implementation. |
| FX calculation | MASAV handles only single currency ILS |
| Posting | MASAV payments has the following outward DD:  - Debit MASAV clearing Nostro account - Credit customer account |

[Process Inward DD Returns](#)

TPH processes the inward DD as follows:

- Enriches the return payment with DD reference item when identifying the original transaction

- Processes the return payment when receiving and mapping the return transaction, and identifying the original payment
- Books the accounting entries for each individual DD return by switching the debit and credit accounts in the original payment and taking the original credit value date as debit value date
- The accounting entries for the return payment are as follows:
  - Debit DD control suspense account (debit value date – original payment credit value date)
  - Credit clearing suspense account (processing date)

- Creates settlement transaction directly
- Generates the accounting entries for the settlement entry to the Nostro account as follows:
  - Debit clearing suspense account (processing date)
  - Credit clearing Nostro account (processing date)