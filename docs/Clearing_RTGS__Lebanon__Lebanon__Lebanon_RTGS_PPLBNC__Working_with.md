# Working with Lebanon RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Lebanon/Lebanon_RTGS_PPLBNC/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Lebanon > [Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm) > Working with

- Lebanon;)
  - [Lebanon RTGS Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Introduction](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Configuration](../../Lebanon/Lebanon_RTGS_PPLBNC/Configuration.htm)
    - [Working with](../../Lebanon/Lebanon_RTGS_PPLBNC/Working_with.htm)
    - [Tasks](../../Lebanon/Lebanon_RTGS_PPLBNC/Tasks.htm)
    - [Outputs](../../Lebanon/Lebanon_RTGS_PPLBNC/Outputs.htm)
  - [Lebanon Cheque Clearing Lebanon Cheque Clearing](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm)

Payments

# Working with Lebanon RTGS

Updated On 08 November 2022 |
 4 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of Lebanon RTGS.

## Manual Capture of Bank Transfers

TPH provides provision to capture bank transfers from OE page. The OE payment allows an Operator to impose a number of values that override the configuration in the payment engine.

- The back office users initiate the bank transfers.
- TPH OE is a generic Payment Order capture page, and not specific to Lebanon RTGS.

- Enter the required details in the following fields:

| Field Name (Label) | Type | M or O | Remarks |
| --- | --- | --- | --- |
| *Priority* | Numeric | M | Can have values between 1 and 9. Depends on the bank requirement. This value is prefixed with 000 and populated in tag 113, which is the priority code of the outgoing SWIFT message. |
| *Output Channel* | Text | O | LBRGS Channel can be selected and imposed while capturing the Lebanon RTGS payment.  - If not imposed, the system selects LBRTGS channel automatically during product determination. |
| *Transaction Currency* | Currency | M | LBP |
| *Transaction Amount* | Amount | M | It can be any valid amount and has no maximum limit |
| *Execution Date* | Date | O |  |
| *Receiver Institution* | Text | M | A valid BIC |
| *Debit Account Number* | Account number | M | Account number from which the funds are debited for payment. |
| *Debit Account Address* |  | M | Debit account holder address. |
| *Debtor Agent Bank* |  | M | BIC |
| *Intermediary Institution Account* |  | O |  |
| *Intermediary Institution Address* |  | O |  |
| *Intermediary Institution Bank Code* |  | O | BIC |
| *Account with Institution Bank Code* |  | O | BIC |
| *Account with Institution Address* |  | O |  |
| *Beneficiary Bank BIC* | Text | M | If receiver institution is not provided, this field is mandatory,. |
| *Beneficiary Account* | Account number | M | Maximum 34 characters. Account number of the beneficiary to whom the funds are sent. |
| *Beneficiary Name* | Text | M | Maximum 70 characters. Name of the beneficiary. |
| *Beneficiary Bank Address* |  | O |  |
| *Additional Information* |  | O | Sender to receiver information |

## Manual Capture of Customer Transfers

TPH provides provision to capture customer transfers from its OE page. The OE payment allows an Operator to impose a number of values that override the configuration in the payment engine.

TPH OE is a generic Payment Order capture page and not specific to Lebanon RTGS.

In addition to the above fields, the following details can be fetched from the OE page:

| Field Name (Label) | Type | M or O | Remarks |
| --- | --- | --- | --- |
| *Charge Option* | Text | O | BEN, SHA or OUR |
| *Charges* |  | O | Amount, currency, and account details |

## LEBANON RTGS Payments Enquiry

The user can perform the following actions in LEBANON RTGS payments:

- To view, use the standard Pending and Processed Paymentsenquiry.
- To filter, search for LBRTGS in *Channel*.

  The user can apply additional filters on other payment attributes.



The screenshot displays the results grid.



The screenshots display the detailed view of the payment.






[Viewing the Generated Output Message](#)

The user can select the required payment and navigate to specific investigation pages based on their requirements. To perform this, do the following:

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Pending and Processed Payments**>**Pending Process Payments – Transaction Wise**.
2. To view the outgoing message of a transaction, select the ‘ViewInDetail’ option, and then ‘Outgoing Message’ from the Options drop-down.



In this topic

- [Working with Lebanon RTGS](#WorkingwithLebanonRTGS)

- [Manual Capture of Bank Transfers](#ManualCaptureofBankTransfers)
- [Manual Capture of Customer Transfers](#ManualCaptureofCustomerTransfers)
- [LEBANON RTGS Payments Enquiry](#LEBANONRTGSPaymentsEnquiry)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:14:00 PM IST