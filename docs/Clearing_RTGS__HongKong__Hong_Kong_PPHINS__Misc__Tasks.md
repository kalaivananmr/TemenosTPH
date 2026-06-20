# Tasks for Hong Kong Faster Payments System (HK FPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/HongKong/Hong_Kong_PPHINS/Misc/Tasks.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Hong Kong > [Hong Kong FPS](../../Hong_Kong_PPHINS/Misc/Introduction.htm) > Tasks

- Hong Kong;)
  - [Hong Kong FPSHong Kong FPS](../../Hong_Kong_PPHINS/Misc/Introduction.htm)
    - [Introduction](../../Hong_Kong_PPHINS/Misc/Introduction.htm)
    - [Configuration](../../Hong_Kong_PPHINS/Misc/Configuration.htm)
    - [Working with](../../Hong_Kong_PPHINS/Misc/Working_with.htm)
    - [Tasks](../../Hong_Kong_PPHINS/Misc/Tasks.htm)
    - [Outputs](../../Hong_Kong_PPHINS/Misc/Outputs.htm)
  - HKICL Cheque Clearing;)
  - CHATS MX Clearing;)
  - FPS Batch Clearing;)
  - CHATS Clearing Directory Upload and Reachability Check;)
  - HKFPS Instant and Batch Clearing Directory;)

Payments

# Tasks for Hong Kong Faster Payments System (HK FPS)

Updated On 07 August 2025 |
 2 Min(s) read

Feedback
Summarize

Hongkong Faster Payment System (HK-FPS or FPS) is a 24x7 instant payment processing system that processes domestic payments within Hongkong. HK-FPS currently processes both credit transfers and direct debits. It operates in Hong Kong Dollar (HKD) and Chinese Yuan (CNY) currencies and processes retail and corporate payments.

Credit is made available to the beneficiary by the beneficiary bank in real time or near real time, with SLA’s varying from within few seconds to few hours depending on the level of participation of the receiving bank in HK-FPS scheme.

## Workflow

HKFPS payments are initiated through `PAYMENT.ORDER` application based on the inputs given by the user or can be imposed by the user in Temenos Payments Hub (TPH).

[Initiating HKFPS Payment](#)

To initiate HKFPS transaction, follow the below steps:

1. Log in as **PAYUSER1** > **Payment Order** > **Input Payment Order** > **Hong Kong** > **Faster Payments (Single)**.
2. Select the transaction currency from the *Debit Currency* field.
3. Enter values in the following fields:
   - *Payment Currency*
   - *Payment Amount*
   - *Debit Account Number*
   - *Beneficiary Account No*
   - *Beneficiary Name*
   - *Beneficiary Bank NCC*
   - *Payment Type*
   - *Payment Sub Type Code*
   - *Beneficiary Proxy ID type*
4. Click the **Validate** icon
5. Click the **Commit** icon.

   Transaction is committed. A transaction reference is created and sent for authorisation.

[Authorising HKFPS Payment](#)

HKFPS payment initiated must be approved for further processing. Payment must be approved in TPH.

To authorise HKFPS payment, follow the below steps:

1. Log in as **PAYUSER7** > **Payment Order** > **Authorise/Delete Payment Order** > **Authorise/Delete Payment Order**.
2. Click the **Authorise** icon corresponding to a transaction.

   Authorise screen is displayed.
3. Verify the details and click **Authorise** icon.

   Transaction is authorised, if no error message displayed.

In this topic

- [Tasks for Hong Kong Faster Payments System (HK FPS)](#TasksforHongKongFasterPaymentsSystemHKFPS)
  - [Workflow](#Workflow)

Related topics:

- [Execute Cancellation Request from Clearing (HK-FPS)](https://tlcengine.temenos.com/Content/MarkedId/4ACDC7E6-B017-4E77-A823-A713E722DEC9)
- [Execute Inward Credit Transfer (HK-FPS)](https://tlcengine.temenos.com/Content/MarkedId/36D90D95-793F-4293-B54C-1473266C76D9)
- [Initiate Outward Cancellation Requests (HK-FPS)](https://tlcengine.temenos.com/Content/MarkedId/2235C14A-4AA6-45E6-9BB0-18F370EFA91D)
- [Receive and Execute Outward Remittance (HK-FPS)](https://tlcengine.temenos.com/Content/MarkedId/7F76DF47-D9DB-47ED-B5A9-CC75B639CDB9)
- [Response to Cancellation Request from Clearing (HK-FPS)](https://tlcengine.temenos.com/Content/MarkedId/45244465-4E74-455A-9A87-DB231710502D)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:15:09 PM IST