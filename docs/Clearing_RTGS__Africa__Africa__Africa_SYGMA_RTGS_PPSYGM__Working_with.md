# Working with SYGMA RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYGMA_RTGS_PPSYGM/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm) > Working with

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
    - [Introduction](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
    - [Configuration](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Configuration.htm)
    - [Working with](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Working_with.htm)
    - [Tasks](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Tasks.htm)
    - [Outputs](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Outputs.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Working with SYGMA RTGS

Updated On 23 May 2023 |
 5 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of SYGMA RTGS.

## Manual Capture of Customer Transfers

1. To manually capture customer transfer, go to **User Menu**>**Payments**>**Payment Order Menu**>**Input Payment Order**>**Payment Order SYGRTGS).**

2. The PO application offers a SYGMA payment capture page to perform the following:

- Validates the payment details (entered by the user) in interactive mode.
- On successful validation, it displays the applicable payment charges and execution date.
- On submission of the payment, it is sent for Supervisor’s approval.
- On approval, it release the payment to the STP processing flow.

To know more, refer to [Outward Processing Flow](Introduction.htm#Outward) section.

The following are the important fields on the SYGMA Transfer page:

| Field | Type | Mandatory/Optional (M/O) | Remarks |
| --- | --- | --- | --- |
| **Main Version Screen** | | | |
| *Payment Order Product* | Fixed value ‘SYGMA’ | M | Defaulted and disabled |
| *Debit Account No* | Account number | M | Any valid Temenos Transact account number |
| *End to End Reference* | Text | O | Maximum 31 characters |
| *Payment Currency* | Currency | M | Currency needs to be XAF |
| *Payment Amount* | Amount | M | Amount can be any valid amount and does not have maximum limit |
| *Payment Execution Date* | Date | M | Defaulted to current business date |
| *Debtor Agent Clearing Code* | BIC | O | BIC code of the debtor agent |
| Beneficiary Details (Sub Tab) | | | |
| *Beneficiary ID* | Standard Temenos Transact field | O | Drop-down menu |
| *Beneficiary Account No* | Local account number | M | Maximum 34 characters |
| *Beneficiary Name* | Text | M | Maximum 70 characters |
| *Beneficiary Country Code* | Text | M | Defaulted to CM |
| *Beneficiary Bank Clearing Code* |  | M | If BIC is provided, this can be left blank |
| *Beneficiary Bank BIC* | BIC | M | Valid BIC. If sort code is provided, this can be left blank |
| **Charge Details (Sub Tab)** | | | |
| *Charge Bearer* | Drop-down menu It allows the following values: BEN, OUR, SHA. | M | Defaulted to `PO` application product setup |
| *Charges* | Amount and Currency | C | Calculated by the system (using TPH simulation) |
| Ordering Details (Sub Tab) | | | |
| *Ordering Customer* | Customer | O | Customer of the Debit Account. Defaulted by the system |
| *Ordering Customer Name* | Text | O | Name of the Ordering Customer |
| *Ordering Reference* | Text | O | Free text (35) |






## Manual Capture of Bank Transfers

To capture the bank transfers from the Order Entry page in TPH, go to **User Menu**>**Payments**>**Payment Hub**>**Initiate Payment Transaction**>**Initiate Customer Transfer**.The Order Entry (OE) payment allows an Operator to impose a number of values to override the configuration in the payment engine.

The following fields are available in the Order Entry page:

| Field | Type | M/O | Remarks |
| --- | --- | --- | --- |
| *Priority* | Numeric | M | If Temenos Transact bank is SYGMA direct participant, the value is 6 |
| *Output Channel* | Text | M | Channel needs to be SYG (configured for SYGMA direct participation) |
| *Transaction Currency* | Currency | M | Currency needs to be XAF |
| *Transaction Amount* | Amount | M | Amount can be any valid amount (no maximum limit) |
| *Execution Date* | Date | M | Defaults to current date |
| *Receiver Institution* | Text | M | Needs to be a valid BIC |
| *Debit Account Number* | Account number | M | Accepts value as defined in `ACCOUNT` table |
| *Debtor Agent Bank* |  | M | BIC value |
| *Intermediary Institution Account* |  | O | Only for NCC |
| *Intermediary Institution Address* |  | O | Valid BIC value |
| *Intermediary Institution Bank Code* |  | O | BIC value |
| *Account with Institution Bank Code* |  | O | BIC value |
| *Account with Institution Address* |  | O | BIC is available |
| *Beneficiary Bank BIC* | Text | M | It is mandatory, when the receiver institution is not available |
| *Beneficiary Account* | Account Number | M | Maximum 34 characters |
| *Beneficiary Name* | Text | M | Maximum 70 characters |
| *Beneficiary Bank Address* |  | O | Free text field for input |
| *Additional Information* |  | O | Sender to Receiver information |



## SYGMA RTGS Payments Enquiry

1. To view SYGMA RTGS payments, go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Pending and Processed Payments**>**Pending Process Payments – Transaction Wise**.
2. To filter SYGMA RTGS payments, search for SYG in *Channel*.

   It also allows to apply advanced filters on the payment attributes.



[Results Grid](#)



[Detailed View of the Payment](#)



## View the SYGMA RTGS Output Message

1. To view the generated SYGMA RTGS output message, go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Pending and Processed Payments**>**Pending Process Payments – Transaction Wise**.
2. To search for the respective transaction, click  and then select ‘Outgoing Message’ from the *Options* drop-down.



In this topic

- [Working with SYGMA RTGS](#WorkingwithSYGMARTGS)

- [Manual Capture of Customer Transfers](#ManualCaptureofCustomerTransfers)
- [Manual Capture of Bank Transfers](#ManualCaptureofBankTransfers)
- [SYGMA RTGS Payments Enquiry](#SYGMARTGSPaymentsEnquiry)
- [View the SYGMA RTGS Output Message](#ViewtheSYGMARTGSOutputMessage)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:46 PM IST