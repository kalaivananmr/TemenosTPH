# Working with Liquidity Transfer Advice

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm

---

2. [Payments](../../../../content/payments.html)

- Europe;)

Payments

# Working with Liquidity Transfer Advice

Updated On 22 March 2025 |
 5 Min(s) read

Feedback
Summarize

The following sections explain how to view, process, and repair the received LTA.

## Viewing LTA File Received in Temenos Payments Hub

To view the LTA files received at Temenos Payments Hub , go to **User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Received and SentFile Details** > **Received File Details** > **Received Message/File Details List**

The user can identify the LTA message based on the File Header Sending Institution, Originating Source and Message Format.

[Viewing LTA Failed at File Level](#)

The user can reject or accept the file. The user can click  to view the LTA that is failed or accepted at the file level. In case of the failed LTA, the *Message/File Status* field gets updated as ‘REJECTED’ and the *Error Code* and *Error Information* fields display the reason for the file level validation failure.



[Viewing LTAs Accepted at File Level](#)

For the accepted LTA, the value of the *Message/File Status* field displays as ‘MAPPED’.



## Viewing LTA Transaction in Temenos Payments Hub

To view the LTA received in Temenos Payments Hub and cleared file level validation,

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **Liquidity Advices** > **LTA Enquiry.**
2. In the selection criteria, enter values in any of the fields such as *OriginatingSource*, *FTNumber* and so on.



[Viewing Successfully Processed LTA](#)

LTA that are successfully qualified as a payment and able to resolve the internal account based on the external account received moves to status code: 999.



Click  to view the LTA payment.



Click  to view details specific to Audit Trail, Accounting Entries and Posting Lines.

The below screenshots show the details specific to Audit Trail.






The below screenshot shows the details specific to Accounting Entries.



The below screenshot shows the details specific to Posting Lines.



[Viewing Failed LTA](#)

To view the LTA that are in Status Code = 235, and in repair queue, click .



The Error Information tab displays the reason behind the transaction falling in Repair Queue.



## Repairing Failed LTA

To repair LTA that cleared file level validation but failed at transaction level,

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **Liquidity Advices** > **LTA Repair.**

Transactions that are in Status Code – 235 are available for repair.



2. Click  to repair the payment. The user can edit the *Debit Account*, *Credit Account* and *Value Date* fields and submit the record.

[Cancelling LTA from Repair Screen](#)

To cancel the LTA,

1. On the Error Information tab, enter the reason in the *Cancel Description* field.
2. Click  to submit.





To authorise the record,

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **Liquidity Advices** > **Authorise LTA Payments**.

This enquiry lists the transaction that are in Status Code = 315.



2. To authorise a record, click .



The payment moves to Status Code = 997.

To view details specific to Audit Trail,

1. In the LTA Auth List page, click  across the record.
2. From the drop-down, select **Audit Trail** and click .



[Approving LTA from Repair Screen](#)

The user can edit the *Debit Account*, *Credit Account* and *Value Date* fields and submit the record.



To authorise the record,

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **Liquidity Advices** > **Authorise LTA Payments**.

The LTA Auth List page lists the transaction that are in Status Code = 315.



2. Click  to authorise a record.



After authorisation, the transaction moves to Status Code = 999.



To view details specific to Audit Trail, Accounting Entries and Posting Lines,

1. In the LTA Auth List page, click  across the record.
2. From the drop-down, select Audit Trail, Accounting Entries, or Posting Lines and click .

The below screenshots show the details specific to Audit Trail.





The below screenshot shows the details specific to Accounting Entries.



The below screenshot shows the details specific to Posting Lines.



In this topic

- [Working with Liquidity Transfer Advice](#WorkingwithLiquidityTransferAdvice)

- [Viewing LTA File Received in Temenos Payments Hub](#ViewingLTAFileReceivedinTemenosPaymentsHub)
- [Viewing LTA Transaction in Temenos Payments Hub](#ViewingLTATransactioninTemenosPaymentsHub)
- [Repairing Failed LTA](#RepairingFailedLTA)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:23:26 PM IST