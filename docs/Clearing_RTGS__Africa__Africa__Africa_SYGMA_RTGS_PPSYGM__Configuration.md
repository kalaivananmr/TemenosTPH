# Configuring SYGMA RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYGMA_RTGS_PPSYGM/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm) > Configuration

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

# Configuring SYGMA RTGS

Updated On 23 May 2023 |
 3 Min(s) read

Feedback
Summarize

TPH bank can be a direct participant of SYGMA RTGS .The channel through which it routes the payment determines the participation type in TPH. To know more on clearing configuration, refer to Clearing Framework section.

## Direct Participant of SYGMA RTGS

1. To configure, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing**.


2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Swift Based* | Set to Y as SYGMA RTGS is a SWIFT-based clearing |
   | *Settlement Type* | Set to GROSS as SYGMA RTGS is an RTGS settlement system |
   | *Service Identifier* | Set to SYG to populate in the tag 103 of the outgoing message (which denotes SYGMA RTGS payment) |
   | The above fields are important elements of a payment in clearing that determine its uniqueness and behavior. | |
   | *Clearing Country Code* | Set to CF as the country code for Central African Republic is CF |
   | *RTGS system* | Set to Y as SYGMA RTGS is a RTGS system |
   | *Skip Reachability* | Set to N as reachability check is not required for SYGMA RTGS system |
   | *Clearing File Transaction Indicator* | Set to T as SYGMA RTGS is based on the transaction |
   | *Clearing Currency* | Set to XAF as TPH currently supports only XAF currency for SYGMA RTGS payments |
3. To define further characteristics of the payment based on direction, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing Setting**.

   The below screen shows the setup for Outgoing MT103 & 202 messages.





   The user can configure the message types (MT103, MT202) and directions of payments (incoming and outgoing can be appropriately mentioned). The above screenshots provide details for both the message types.
4. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Message Direction* | Direction of the payment for which the Clearing Setting record needs to be created. This can be configured as R and S for MT103 and MT202 to receive and send, respectively. |
   | *Clearing Account Number* | Clearing account (Nostro) of the clearing in the clearing currency. |
   | *Message Payment Type* | Type of message for which the clearing setting record needs to be created. For example, 103, 202, etc. This is used for the messages 103 and 202 in SYGMA RTGS clearing. |

## Clearing Cut-Off

To configure different cut-off times for customer transfer (MT103) and bank transfer (MT202), go to **Admin Menu**>**Payments Hub**>**Routing & Settlement**>**Channel Cutoff**.



In this topic

- [Configuring SYGMA RTGS](#ConfiguringSYGMARTGS)

- [Direct Participant of SYGMA RTGS](#DirectParticipantofSYGMARTGS)
- [Clearing Cut-Off](#ClearingCutOff)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:33:45 PM IST