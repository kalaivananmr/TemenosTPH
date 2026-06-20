# Working with SGMEPS in ISO20022 (MX)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Singapore/Singapore/PPSGMX/WorkingWith.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Singapore > SGMEPS in ISO20022 (MX) > Working with

- Singapore;)
  - SGMEPS in ISO20022 (MX);)
    - [Introduction](../../Singapore/PPSGMX/Introduction.htm)
    - [Configuration](../../Singapore/PPSGMX/Configuration.htm)
    - [Working with](../../Singapore/PPSGMX/WorkingWith.htm)
    - [Tasks](../../Singapore/PPSGMX/Tasks.htm)
    - [Outputs](../../Singapore/PPSGMX/Outputs.htm)

Payments

# Working with SGMEPS in ISO20022 (MX)

Updated On 12 April 2026 |
 31 Min(s) read

Feedback
Summarize

This module covers the following functionalities:

## Understanding of Outward Customer Credit Transfer

The process flow of the outgoing pacs.008 message are described below.
When the debtor agent initiates the customer credit transfer via the POA (Payment Order Application) or OE (Order Entry) screen, with currency SGD, the system processes the customer-initiated transfer. Upon successful validation, the pacs.008 message is generated and sent to clearing via SWIFT.
The following examples are provided for a better understanding of how the payments initiated through POA (Payment Order Application).

[Process SG MEPS+ Outward customer transfer payments initiated using Payment Order with INTINS roles](#)

This section explains how to process SG MEPS+ Outward customer transfer payments initiated using Payment Order with INTINS roles.

Initiate pacs.008 from PAYMENT.ORDER,MEPS.CUST with INTINS roles and input the Creditor Agent with the *BICFI*, *Name*, and *Postal Address* fields to initiate payment as non-STP as shown below.















The payment moves to 999 after running the Heavy service as shown below.



On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

[SFD-BR109365LGHJDDBH.xml](../XML/SFD-BR109365LGHJDDBH.xml)

[Processing SG MEPS+ Outward Customer Transfer Payment (STP) initiated using Payment Order with below inputs](#)

This section explains the processing of an SG MEPS+ Outward Customer Transfer (STP), initiated using Payment Order with the following:

- Addresslines for Intermediary agents 2 and 3 and RelatedRemittanceInformation
- Input name for party and agent roles (with 140 characters)
- Only names should be inputted for Cdtr, Dbtr, InitgPty, UltmtCdtr, and UltmtDbtr

1. Initiate a payment through MEPS payment order version (PAYMENT.ORDER,MEPS.CUST).












2. Commit and authorise the payment as shown below.








   The screen below shows that the payment has been processed successfully.

   The user can view the payment details in the **View Screen** as shown below.

   **Audit Trail:** [Audit-Trail\_2901261048521549815127000.html](../1/Audit-Trail_2901261048521549815127000.html)
   An Outward pacs.008 file is generated in the DEOutwardInteg folder, after running the BNK/INTEGRATION.SERVICE: [SFD-BNK09362HFHBDFLG.xml](../1/SFD-BNK09362HFHBDFLG.xml)

[Verifying Special Character Mapping in Outward pacs.008 (non-STP) initiated using pain.001 for the mentioned Parties and Agents](#)

This section explains how to verify special character mapping in an Outward pacs.008 (non-STP) initiated using pain.001 for the following parties and agents:

- Initiating party (Addresslines)
- Debtor
- Debtor Agent
- Creditor
- Creditor Agent
- Instructing Agent
- Instructed Agent
- Ultimate Debtor (Addresslines)
- Ultimate Creditor (Addresslines)
- IntermediaryAgent2 (Addresslines)
- IntermediaryAgent3 (Addresslines)
- Related Remittance Information (Addresslines)

1. Initiate an Inward pain.001 message from the PP/BulkCTIInput folder: [MEPS-PAIN001-KPS171080448984-001.xml](../1/MEPS-PAIN001-KPS171080448984-001.xml)
   The file is mapped in the **Received File Details** tab as shown below.

2. Run the BNK/PAYMENT.STPFLOW.MEDUIM service, after which the payment moves to status 999 as shown below.

   The user can view the payment details in the **View Screen** as shown below.

   An Outward pacs008 file is generated in the PP/DEOutwardInteg folder: [SFD-BR109362BKCMKFKF.xml](../1/SFD-BR109362BKCMKFKF.xml)

[Initiating Outward pacs.008 Messages through pain.001 (non-STP) with *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to initiate Outward pacs.008 messages through pain.001 (non-STP) with *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Initiate an Inward pain001 message from the PP/BulkCTIInput folder: [MEPS-PAIN001-MPS171080448984-001.xml](../1/MEPS-PAIN001-MPS171080448984-001.xml)
   The file is mapped in the **Received File Details** tab as shown below.

2. Run the BNK/PAYMENT.STPFLOW.MEDIUM service, after which the payment moves to status 999 as shown below.

   The user can view the payment details in the **View Screen** as shown below.

   An Outward pacs.008 file is generated in the PP/DEOutwardInteg folder: [SFD-BR109362JFK0MDDL.xml](../1/SFD-BR109362JFK0MDDL.xml)

[Initiating Outward pacs.008 Messages through POA (non-STP) with *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to initiate Outward pacs.008 messages through POA (non-STP) with *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Initiate a payment through the MEPS payment order version (PAYMENT.ORDER,MEPS.CUST).














2. Commit and authorise the payment as shown below.








   The payment is processed as shown in the screen below.

   The user can view the payment details in the **View Screen** as shown below.

   **Audit Trail:** [Audit-Trail\_0302261736376114990680000.html](../1/Audit-Trail_0302261736376114990680000.html)
3. Run the BNK/INTEGRATION.SERVICE service, after which an Outward pacs.008 file is generated in the DEOutwardInteg folder: [SFD-BNK09362FJGMJFGB.xml](../1/SFD-BNK09362FJGMJFGB.xml)

[Initiating Outward pacs.008 Messages through OE (non-STP) with *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to initiate Outward pacs.008 messages through OE (non-STP) with *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Initiate an outward pacs.008 through the PP.ORDER.ENRTY,CTR.ISO.O version.
























2. Commit and authorize the record, after which an Outward pacs.008 payment is created in status 600.

3. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999.

4. Run the BNK/INTEGRATION.SERVICE service, after which an outward pacs.008 file is generated: [SFD-BNK09362FFHMHGGL.xml](../1/SFD-BNK09362FFHMHGGL.xml)

[Verifying Special Character Mapping in Outward pacs.009 (OE) for the mentioned Parties and Agents](#)

This section explains how to verify special character mapping in an Outward pacs.009 (OE) for the following parties and agents:

- Debtor
- Debtor Agent
- Creditor
- Creditor Agent
- Instructing Agent
- Instructed Agent
- IntermediaryAgent2 (Addresslines)
- IntermediaryAgent3 (Addresslines)

1. Initiate an Outward pacs.009 from the PP.ORDER.ENTRY,BTR.ISO.O version.


















2. Commit the record and authorise the payment, after which it moves to status 999.

   An Outward pacs.009 file is generated in the DEOutwardInteg folder: [SFD-BR109362FKMDJJLK.xml](../1/SFD-BR109362FKMDJJLK.xml)

### Outward Financial Institution Credit Transfer

This section explains how to process the outward financial institution credit transfers.

[Process SG MEPS+ Outward Bank transfer payments initiated using Payment Order using INTINS roles](#)

This section explains how to process SG MEPS+ Outward bank transfer payments initiated using Payment Order with INTINS roles.

Initiate pacs.009 from PAYMENT.ORDER,MEPS.BANK with INTINS roles as shown below.











The payment moves to 999 after running the Heavy service as shown below.



On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

[SFD-BR109365LDLGBBLB.xml](../XML/SFD-BR109365LDLGBBLB.xml)

[Process SG MEPS+ Outward Bank Transfer Payment initiated using Payment Order using INTINS roles with only Creditor BIC](#)

This section explains how to process SG MEPS+ Outward Bank Transfer Payment initiated using Payment Order. The user must input only Creditor BIC and not the Creditor Agent BICFI.

Initiate a payment through MEPS payment order version PAYMENT.ORDER,MEPS.BANK with Only Creditor BIC as shown below.







The payment moves to 999 after running the Heavy service as shown below.



On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

[SFD-BNK09358DBCGC0JM.xml](../XML/SFD-BNK09358DBCGC0JM.xml)

[Processing SG MEPS+ Outward Bank Transfer Payment initiated using Order Entry with the following Inputs](#)

This section explains how to process the SG MEPS+ Outward Bank Transfer initiated using Order Entry with the following:

- Addresslines for Intermediary agents 2 and 3
- Input name for party and agent roles (with 140 characters)
- InputEndtoEnd ID (with 35 characters)

1. Process the Outward pacs.009 from PP.ORDER.ENTRY,BTR.ISO.O or by navigating to **User Menu** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer**.








2. Commit the record.

3. Navigate to **User Menu** > **Payment Approvals** > **Authorise Pending Payments** > **Auth, Order Entry, and Repair Payments** > **Pending Authorise Payments** and authorise the record.






4. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999.
   The user can view the payment details in the **View Screen** a shown below.

   **Audit Trail:** [Audit-Trail\_3101260933593233138603000.html](../1/Audit-Trail_3101260933593233138603000.html)
5. Run the BNK/INTEGRATION.SERVICE service, after which an outfile is generated in the DEOutwardInteg folder: [SFD-BNK09362BJC0MBKK.xml](../1/SFD-BNK09362BJC0MBKK.xml)

[Initiating Outward pacs.009 Messages through POA with *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to initiate Outward pacs.009 messages through POA with *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Process the Outward pacs.009 from PP.ORDER.ENTRY,BTR.ISO.O or by navigating to **User Menu** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer**.












2. Commit the record.

3. Navigate to **User Menu** > **Payment Approvals** > **Authorise Pending Payments** > **Auth, Order Entry, and Repair Payments** > **Pending Authorise Payments** and authorise the record.  

4. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999 as shown below.

   The user can view the payment details in the **View Screen** as shown below.

   **Audit Trail:** [Audit-Trail\_0602260947338425862412000.html](../1/Audit-Trail_0602260947338425862412000.html)
5. Run the BNK/INTEGRATION.SERVICE service, after which an outfile is generated in the DEOutwardInteg folder: [SFD-BNK09362BJHFB0MD.xml](../1/SFD-BNK09362BJHFB0MD.xml)

## Outward Financial Institution Credit Transfer Cover

This section explains how to process the outward financial institution credit transfer covers.

[Process Outward pacs.009COV from PAYMENT.ORDER,ISO.SWIFT.INPUT with INTINS Roles](#)

This section explains how to process the outward pacs.009COV from PAYMENT.ORDER,ISO.SWIFT.INPUT with INTINS roles.

Initiate pacs009cov from PAYMENT.ORDER,ISO.SWIFT.INPUT as shown below.















The payment moves to 999 after running the Heavy service as shown below.



On running the Integration service, SWIFT pacs.008 and pacs.009COV are generated in the DEOutwardInteg folder.

[SFD-BR109365HFHLHLDL.xml](../XML/SFD-BR109365HFHLHLDL.xml)

[SFD-BR109365HFHLHLDL-COV.xml](../XML/SFD-BR109365HFHLHLDL-COV.xml)

[Initiating Outward pacs.009 COV from POA screen (PAYMENT.ORDER,ISO.SWIFT.INPUT)](#)

This section explains how to initiate an Outward pacs.009 COV from the POA screen (PAYMENT.ORDER,ISO.SWIFT.INPUT) with the following:

- Addresslines for Intermediary agents 2 and 3, and UndrlygCstmrCdtTrf/IntrmyAgt2&3
- Input name only for party roles (with 140 characters) - UndrlygCstmrCdtTrf Cdtr, Dbtr, UltmtCdtr, and Ultmtdbtr

1. Initiate an Outward pacs.009cov from the PAYMENT.ORDER,ISO.SWIFT.INPUT version.














2. Commit the record and authorise the payment, after which it moves to status 999.

3. Run the BNK/INTEGRATION.SERVICE service, after which the Swift pacs.008 and Sgmeps pacs.009cov files are generated in the DEOutwardInteg folder.
   - **Swift pacs.008:**[SFD-BR109362BJKB00CC.xml](../1/SFD-BR109362BJKB00CC.xml)
   - **SGMEPS pacs.009cov:**[SFD-BR109362BJKB00CC-COV.xml](../1/SFD-BR109362BJKB00CC-COV.xml)

[Initiating Outward pacs.008 SWIFT Payment with underlying Cover Payment pacs.009COV (with 3 Reimbursement Agent Tags) - Processed through CHAPS Clearing](#)

This section explains how to initiate an Outward pacs.008 SWIFT payment, with underlying pacs.009COV (with 3 Reimbursement Agent tags) – processed through the CHAPS Clearing.

1. Process the Outward pacs.009COV from PP.ORDER.ENTRY,CTR.ISO.O or navigating to **User Menu** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer**.














2. Commit and authorise the record, after which a payment is created in status 600.

3. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999.

   The user can view the payment details in the **View Screen** tab as shown below.

4. Run the BNK/INTEGRATION.SERVICE service, after which a Swift pacs.008 and pacs.009cov files are generated in the DEOutwardInteg folder.
   - **Swift pacs.008**: [SFD-BNK09362HFDCK0DD.xml](../1/SFD-BNK09362HFDCK0DD.xml)
   - **pacs.009cov**: [SFD-BNK09362HFDCK0DD-COV.xml](../1/SFD-BNK09362HFDCK0DD-COV.xml)

### Receive and Process Inward pacs.008 Customer Credit Transfer

TPH receives Incoming Customer credit transfer Pacs.008 message. TPH validates the payment message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation)

After running heavy service, payment status should be updated to 999.
On successful validation, TPH performs accounting entry posting:

- Debit – MEPS+ Clearing Nostro
- Credit – Beneficiary Customer Account

[Receive and process inward pacs.008 with Posting restriction on the beneficiary account and verify validation at TPH](#)

TPH receives Incoming Pacs.008 message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation,). After successful validation the payment get mapped.

After running heavy weight service, the payment status moves due to posting restriction in credit account to 235 status.

Audit trail is updated with posting restriction details. After removing account restriction,open the payment from OE (Order Entry) screen - repair and system should allow to commit the payment without any error.

1. Process inward pacs.008 msg through **DEInwardInteg**. [SGMEPS\_Inward\_pacs.008\_0091.xml](../../Resources/Images/Singapore/PPSGMX/Files/SGMEPS_Inward_pacs.008_0091.xml)
2. Payment is created at status 4. After running **BNK/PAYMENT.STPFLOW.HEAVY** service, payment moves to 235 with posting restriction in credit account.
3. Audit Trail is updated with details of posting restriction.
4. Remove posting restriction then repair the payment from following menu.
5. Commit and authorize - **PP.ORDER.ENTRY,REP.CTR.ISO** screen


6. Payment moves to 999 status.
7. Audit Trail is updated.
8. **POR .SUPPLEMENTARY.INFO** and **POR.TRANSACTION** table record is updated. [POR.SUPPLEMENTARY.INFO S BNK24137M0KH00CK.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137M0KH00CK.pdf)
   [POR.TRANSACTION S BNK24137M0KH00CK.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK24137M0KH00CK.pdf)

[Receive and process inward pacs.008 with duplicate reference number.](#)

TPH receives Incoming Pacs.008 message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation,). After successful validation the payment get mapped.

After running heavy weight service, the payment status moves due to posting restriction in credit account to 235 status.

Audit trail is updated with posting restriction details. After removing account restriction,open the payment from OE (Order Entry) screen - repair and system should allow to commit the payment without any error.

1. Process inward pacs.008 msg through **DEInwardInteg**. [SGMEPS\_Inward\_pacs.008\_0091.xml](../../Resources/Images/Singapore/PPSGMX/Files/SGMEPS_Inward_pacs.008_0091.xml)
2. Payment is created at status 4. After running **BNK/PAYMENT.STPFLOW.HEAVY** service, payment moves to 235 with posting restriction in credit account.
3. Audit Trail is updated with details of posting restriction.
4. Remove posting restriction then repair the payment from following menu.
5. Commit and authorize - **PP.ORDER.ENTRY,REP.CTR.ISO** screen


6. Payment moves to 999 status.
7. Audit Trail is updated.
8. **POR .SUPPLEMENTARY.INFO** and **POR.TRANSACTION** table record is updated. [POR.SUPPLEMENTARY.INFO S BNK24137M0KH00CK.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137M0KH00CK.pdf)
   [POR.TRANSACTION S BNK24137M0KH00CK.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK24137M0KH00CK.pdf)

[Processing Incoming pacs.008 message (non-STP) and Verifying Validation at TPH](#)

This section explains how to:

1. Process an Incoming pacs.008 non STP message with the following:
   - Addresslines for Previous Instructing agents 2 and 3 and RelatedRemittanceInformation
   - Name for party and agent roles (with 140 characters)
   - <BizSvc>mas.mep.02</BizSvc>
   - Only names should be inputted for Cdtr, Dbtr, InitgPty, UltmtCdtr, and UltmtDbtr
2. Verify validation at TPH

1. Process the Incoming Non STP pacs.008 message in the PP\DEInwardInteg folder: [inward-PACS008-SGMEPS-NONSTP-5048.xml](../1/inward-PACS008-SGMEPS-NONSTP-5048.XML)
   The file is mapped in the **Received File Details** tab as shown below.

   A payment is created at status 4.
2. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999.

   **Audit Trail:** [POR.AUDIT.TRAIL\_3.1a.pdf](../1/POR.AUDIT.TRAIL_3.1a.pdf)

[Processing Incoming pacs.008 Message with Hybrid Address - *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to process an Incoming pacs.008 message with Hybrid Address – *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Initiate an Inward pacs.008 message from the PP/DEInwardInteg folder: [inward-PACS008-SGMEPS-5056.xml](../1/inward-PACS008-SGMEPS-5056.XML)
   The file is mapped in the **Received File Details** tab as shown below.

2. Run the BNK/PAYMENT.STPFLOW.HEAVY service, after which the payment moves to status 999.

   The user can view the payment details in the **View Screen** as shown below.

   **Audit Trail:** [POR.AUDIT.TRAIL-BR109362FK0FMBGJ.pdf](../1/POR.AUDIT.TRAIL-BR109362FK0FMBGJ.pdf)

### Receive and process inward pacs.009 Financial institution credit transfer

TPH receives Incoming pacs.009 Financial institution credit transfer message. TPH validates the payment message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation)

After running heavy service, the payment status should be updated to 999
On successful validation, TPH performs accounting entry posting:

- Debit – MEPS+ Clearing Nostro
- Credit – Beneficiary Customer Account

[Processing Incoming pacs.009 Message with Hybrid Address - *Postal Address* of all Structured Address Subtags and *Address Line* of 3](#)

This section explains how to process an Incoming pacs.009 message with Hybrid Address – *Postal Address* of all Structured Address subtags and *Address Line* of 3 (with 70 characters each).

1. Process the Inward pacs.009 file in the DEInwardInteg folder: [SGMEPSMX-PACS009-APS171080449661-001.xml](../1/SGMEPSMX-PACS009-APS171080449661-001.xml)

   The file is mapped in TPH and can be viewed under PPT.RECEIVEDFILEDETAILS as shown below.



   A payment is created in status in 4.
2. Run the BNK/PAYMENT.STPFLOW.MEDIUM service, after which the payment moves the payment to status 999.



   The payment details can be viewed under the **View Screen** as shown below.



















   **Audit Trail:**[POR.AUDIT.TRAIL-BR109362JFGHFJLD.pdf](../1/POR.AUDIT.TRAIL-BR109362JFGHFJLD.pdf)

[Receive and process inward pacs.009 Financial institution credit transfer](#)

1. Process an inward pacs.009 msg through **DEInwardInteg**. [SGMES\_Inward\_pacs.009\_0101.xml](../../Resources/Images/Singapore/PPSGMX/Files/SGMES_Inward_pacs.009_0101.xml)
2. Launch the **User Menu >Payments>Payments Hub>Payments Inquiries> Received Message-List**.
3. The payment is created at status 4. After running **BNK/PAYMENT.STPFLOW.HEAVY** service, payment moves to 999 status.
4. Check if the audit trails have been updated.
5. **POR .SUPPLEMENTARY.INFO** and **POR.TRANSACTION** table record is updated. [POR.SUPPLEMENTARY.INFO S BNK24137DBCBGMBF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137DBCBGMBF.pdf)
   [POR.TRANSACTION S BNK24137DBCBGMBF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK24137DBCBGMBF.pdf)

[Receive and process inward pacs.009 Financial institution with Posting restriction on the beneficiary account and verify validation at TPH](#)

TPH receives Incoming Pacs.009 message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation,). After successful validation, the payment is mapped.

After running heavy weight service, the payment status moves due to posting restriction in credit account to 235 status.

Audit trail is updated with posting restriction details. After removing account restriction, open the payment from OE (Order Entry) screen - repair and system should allow to commit the payment without any error.

1. Process an inward pacs.009 msg through **DEInwardInteg**. [SGMES\_Inward\_pacs.009\_003.xml](../../Resources/Images/Singapore/PPSGMX/Files/SGMES_Inward_pacs.009_003.xml)
2. The payment is created at status 4. After running **BNK/PAYMENT.STPFLOW.HEAVY** service, the payment moves to 235 with posting restriction in credit account.



   Pending and Processed Payments



   Pending and Processed Payments
3. The Audit Trail is updated with details of posting restriction.
4. Remove posting restriction then repair the payment from the following menu:
5. Commit and authorize - **PP.ORDER.ENTRY,REP.CTR.ISO** screen.
6. Payment moves to 999 status.
7. Audit Trail is updated.

[Receive and process inward pacs.009 Financial institution with duplicate reference number](#)

TPH receives Incoming pacs.009 Financial institution message. TPH processes the payment and performs the necessary validation checks (Duplicate check, Account validation,).

TPH processes the payment and performs the Duplicate validation check.

As the <BizMsgIdr> reference is same as previous message, TPH rejects the payment.

**PPT.RECEIVEDFILEDETAILS** application is updated with error as per core behaviour.

1. Process an inward pacs.009 msg through **DEInwardInteg**. [SGMES\_Inward\_pacs.009\_0150.xml](../../Resources/Images/Singapore/PPSGMX/Files/SGMES_Inward_pacs.009_0150.xml)
2. Launch the **User Menu >Payments>Payments Hub>Payments Inquiries> Received Message-List**.

### Initiate Cancellation Request for pacs.008/pacs.009

- The cancellation enquiries for both Customer and Bank initiated cancellations are available under **Payments** > **Payment Hub** > **Investigations and Cancellations** > **Cancellations** > **RTGS Cancellations** > **Create RTGS Cancellation Requests** > **SGMEPS Customer/Bank Initiated Cancellation Request**.
- User can initiate a Recall/Cancellation (camt.056) for an earlier pacs.008/pacs.009/pacs.009 COV message sent to clearing from the enquiry provided.
- User to input the FT Number of the payment to be recalled/Cancelled and click "Cancel"
- Status of the original pacs.008/pacs.009/pacs.009 COV is at 999 status (Completed - Payment Successfully Processed).
- User to specify the Cancel Reason Code (TPH Configurable – Refer Model Configuration, PP. CLEARING.RETURNCODE) & Additional Information for Cancelling the payment & "Submit" the payment.

[Cancellation Request for Outgoing pacs.008 from Customer Initiated Enquiry](#)

1. Process outgoing pacs.008 via PAYMENT.ORDER,MEPS.CUST.



MEPS Customer Transfer




MEPS Customer Transfer




MEPS Customer Transfer




MEPS Customer Transfer

2. Commit and authorize the record
3. Run BNK/PAYMENT.STPFLOW.HEAVY Service for the payment to move to 999.
4. After running **BNK/INTEGRATION.SERVICE** service, outward file will be generated in **DEOutwardInteg** folder. [SFD-BNK241370LGGJGDF.xml](../../Resources/Images/Singapore/PPSGMX/Files/SFD-BNK241370LGGJGDF.xml)
5. Initiate Outward Customer Initiated cancellation request.
6. Provide ISO cancel reason code, commit and authorize the record.
7. Status is updated as cancellation sent.
8. File is generated in **PP/DEOutwardInteg**.
   [PCR24137DFHCG0KL.xml](../../Resources/Images/Singapore/PPSGMX/Files/PCR24137DFHCG0KL.xml)

[Cancellation Request for Outgoing pacs.009 from Bank Initiated Enquiry](#)

1. Process outgoing pacs.009 via PAYMENT.ORDER,MEPS.BANK



MEPS Customer Transfer




MEPS Customer Transfer




MEPS Customer Transfer

2. Commit and Authorize the record.
3. Run **BNK/PAYMENT.STPFLOW.HEAVY** service for the payment to move to 999.
4. After running **BNK.INTEGRATION.SERVICE** outward file gets generated in **DEOutwardInteg**. [SFD-BNK24137FHCFLKKJ.xml](../../Resources/Images/Singapore/PPSGMX/Files/SFD-BNK24137FHCFLKKJ.xml)
5. Initiate Outward Customer Initiated cancellation request.
6. Provide ISO cancel reason code, commit and authorize the record.
7. Status is updated as cancellation sent.
8. File is generated in **PP/DEOutwardInteg**. [PCR24137G0JKMCGJ.xml](../../Resources/Images/Singapore/PPSGMX/Files/PCR24137G0JKMCGJ.xml)

## Inward camt.029, Rejection Notification xsys.003, and Authorization Notification xsys.002

This section explains how to receive and process inward camt.029, rejection notification xsys.003, and authorization natification xsys.002 for the generated pacs.008, pacs.009, or pacs.009 cov payment.

[Process Incoming camt.029 followed by xsys.003 for customer initiated outward camt.056 underlying POA Outward pacs.008 (by selecting 'Reverse' option from RTGS Exception Queue)](#)

This section explains how to process an incoming camt.029 (CNCL) followed by xsys.003 for a customer initiated outward camt.056 underlying POA Outward pacs.008 (STP). The user can select the **Reverse** option from the RTGS Business Exception Queue.

1. Initiate pacs.008 from PAYMENT.ORDER,MEPS.CUST. The payment moves to 999 after running the Heavy service.

2. Navigate to **Payments** > **Payment Hub** > **Investigations and Cancellations** > **Cancellations** > **RTGS Cancellations** > **Create RTGS Cancellation Requests** > **SGMEPS Customer Initiated Cancellation Request** to initiate an outward camt.056.

3. Select the **Cancel By Originator** option.

4. Input the ISO Cancel Reason Code and commit the record. 


   After authorization, the EBQA status is updates as ‘CANCELLATIONSENT’.


   The audit trail details are updated as shown below.


   On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

   [PCR09365BBGFGFMJ.xml](../XML/PCR09365BBGFGFMJ.xml)
5. Process the inward camt.029 CNCL for the sent camt.056 with OrgnlInstrId as the matching criteria.

   [SGMEPS-CAMT029-SMS171080447816-001.xml](../XML/SGMEPS-CAMT029-SMS171080447816-001.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.


   Below is the View screen of the Received File Details.


   The audit trail details are updated as shown below.


   The EBQA status changes to ‘CANCELACCEPTED’ as shown below.


   A record is created in DE.O.HEADER as shown below.


   Below is the View screen of DE.O.HEADER.

6. Process the inward xsys.003 msg with *Carrier Seq No* of pacs.009 in RequestRef tag.

   [SGMEPSMX-XSYS003-SMS171080448718-011.xml](../XML/SGMEPSMX-XSYS003-SMS171080448718-011.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.



   The audit trail details are updated as shown below.


   PSM.BLOB is updated with Acknowledgementcode as ‘1’.


   The user can action the transaction by navigating to **User menu** > **Payments** > **Payment Hub** > **Payment Exception** > **RTGS ISO Exception Queue** > **RTGS Business Exception Queue**.



   The screen below shows the Input Output Channel & FT Number and search.

7. Select the **Reverse** option and commit the record.

8. Navigate to **User menu** > **Payments** > **Payment Hub** > **Payment Approvals** > **Authorise RTGS Exceptions** > **Authorise RTGS Exceptions** to Authorise the payment.

9. Select the **Authorise** option and commit the record.

   When the user selects the ‘Reverse’ option, that is, when the user accepts xsys.003, the accounting entries are reversed and the payment status is moved to 998 (Completed - Payment reversed -rejected) and a Reversal Transaction is created and moved to 999 status.


   The screen below shows the Audit Trail of the original transaction.


   The screen below shows the Accounting entries of the original transaction.


   The screen below shows the Accounting entries of the Reversal transaction.


   The screen above is for underlying Pacs.008. The same flow is followed for underlying Pacs.009 and Pacs.009COV.

[Process Incoming camt.029 (CNCL) followed by xsys.003 for Customer Initiated Outward camt.056 underlying Pain.001 Initiated Outward pacs.008 (by selecting 'Ignore' option from RTGS Exception Queue)](#)

This section explains how to process an incoming camt.029 (CNCL) followed by xsys.003 for a customer initiated outward camt.056 underlying pain.001 initiated Outward pacs.008 (STP). The user can select the **Ignore** option from the RTGS Business Exception Queue.

1. Process the incoming pain.001 message through the BulkCTIInput folder.
   [MEPS-PAIN001-APS100925610202-001.xml](../XML/MEPS-PAIN001-APS100925610202-001.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.


   The payment moves to 999 after running the Medium service.


   Below is the View screen of the Received File Details.



   On running the Integration service, an Outfile is generated in the DEOutwardInteg folder

   [SFD-BNK09365KFM0DGKD.xml](../XML/SFD-BNK09365KFM0DGKD.xml)
2. Navigate to **Payments** > **Payment Hub** > **Investigations and Cancellations** > **Cancellations** > **RTGS Cancellations** > **Create RTGS Cancellation Requests** > **SGMEPS Customer Initiated Cancellation Request** to initiate an Outward camt.056 as shown below.

3. Select the **Cancel By Originator** option.

4. Input the ISO Cancel Reason Code and commit the record.


   After authorization, the EBQA status is updated as ‘CANCELLATIONSENT’ as shown below.


   The screen below shows the audit trail details.


   On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

   [PCR09365JGDHGHKF.xml](../XML/PCR09365JGDHGHKF.xml)
5. Process the inward camt.029 CNCL for the sent camt.056 with OrgnlInstrId as the matching criteria.

   [SGMEPS-CAMT029-pacs008-BPS171080447816-001.xml](../XML/SGMEPS-CAMT029-pacs008-BPS171080447816-001.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.


   Below is the View screen of the Received File Details.


   The EBQA status changes to ‘CANCELACCEPTED’ as shown below.

6. Process the xsys.003 msg with *Carrier Seq No* of pacs.008 in RequestRef tag and with returncode which has routetoexception as 'Y' in PP.CLEARING.RETURNCODE.

   [SGMEPSMX-XSYS003-PACS008-APS171080448738-001.xml](../XML/SGMEPSMX-XSYS003-PACS008-APS171080448738-001.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.



   Below is the View screen of the Received File Details.


   The audit trail details are updated as shown below.

   The Acknowledgementcode is updated as ‘1’ in PSM.BLOB as shown below.


   The user can action the transaction by navigating to **User menu** > **Payments** > **Payment Hub** > **Payment Exception** > **RTGS ISO Exception Queue** > **RTGS Business Exception Queue**.

7. Select the **Ignore** option and commit the record.

8. Navigate to **User menu** > **Payments** > **Payment Hub** > **Payment Approvals** > **Authorise RTGS Exceptions** > **Authorise RTGS Exceptions** to Authorise the payment.

9. Select the **Authorise** option and commit the record.


   The Payment moves to 994 as shown below.


   The audit trail details are updated as shown below.

   The screen below shows the Posting Lines.


   The screen below shows the Accounting Entries.


   The screen above is for underlying Pacs.008. The same flow is followed for underlying Pacs.009 and Pacs.009COV.

[Process Incoming camt.029 followed by xsys.002 for Bank Initiated Outward camt.056 underlying POA Outward pacs.008](#)

This section explains how to process an incoming camt.029 (RJCR) followed by xsys.002 for a bank initiated outward camt.056 underlying POA Outward pacs.008 (non STP).

1. Initiate a pacs.008 payment from PAYMENT.ORDER,MEPS.CUST.


   The payment moves to 999 after running the Heavy service.


   On running the Integration service, an outfile is generated in the DEOutwardInteg folder.

   [SFD-BNK09357BHMLDHDG.xml](../XML/SFD-BNK09357BHMLDHDG.xml)
2. Navigate to **Payments** > **Payment Hub** > **Investigations and Cancellations** > **Cancellations** > **RTGS Cancellations** > **Create RTGS Cancellation Requests** > **SGMEPS Customer Initiated Cancellation Request** to initiate an Outward camt.056 as shown below.


3. Select the **Cancel By Originator Bank** option.

4. Input the ISO Cancel Reason code and submit the record.


   After authorization, on running integration service, an outfile is generated in the DEOutwardInteg folder.
   [PCR09357FBGLJ0LL.xml](../XML/PCR09357FBGLJ0LL.xml)

   The EBQA status changed to ‘CANCELLATIONSENT’ as shown below.


   The screen below shows the Audit trail of the payment.

5. Process the inward camt.029 CNCL for the sent camt.056 with OrgnlInstrId as the matching criteria.

   [SGMEPS-CAMT029\_RJCR-pacs008-VPS171080447830-002.xml](../XML/SGMEPS-CAMT029_RJCR-pacs008-VPS171080447830-002.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.



   The audit trail details are updated as shown below.


   The EBQA status is changed to ‘CANCELREJECTED’ as shown below.


   The record gets created in DE.O.HEADER as shown below.

6. Process the incoming xsys.002 message for the sent pacs.008 message with *Carrier Seq No* as the matching criteria.

   [SGMEPSMX-XSYS002-SKL171080448718-002.xml](../XML/SGMEPSMX-XSYS002-SKL171080448718-002.xml)

   The file is mapped in the Received File Details (ENQ PPT.RECEIVEDFILEDETAILS) as shown below.


   The audit trail details are updated as shown below.


   PSM.BLOB updated with Acknowledgementcode as ‘0’.


   The screen above is for underlying Pacs.008. The same flow is followed for underlying Pacs.009 and Pacs.009COV.

[Receive and Process the Rejection Notification (xsys.003) Message for outward customer payment Pacs.008](#)

TPH receives and processes the xsys.003 message from the clearing. **PT.RECEIVEDFILEDETAILS** – file is updated as **MAPPED**. System maps the xsys.003 for processing using clearing framework.

The process of matching **OriginalTransactionIdentification** is as follows:

- TPH matches the Request Reference field of xsys.003 message with **CARRIER.SEQ.NO** field in **DE.O.HEADER** table and then find the relevant FT number.
- The corresponding FT number should then match with **OriginalTransactionIdentification** value.
- The reject reason code is configured for Straight Through Processing. The system automatically reverses the accounting entries.
- TPH updates the status of the underlying customer payment transaction to 998 (Completed and reversed (payment rejected)).
- TPH updates the audit trail of the underlying customer payment transaction with reason/description of rejection
- Reversal Transaction is created and moved to 999 status.

An example is provided below.

**User Menu>> Payments>>Payment Hub>> Initiate Payment Transaction>Singapore> Initiate MEPS Customer Transfer**

1. Initiate a pacs.008 payment from version **PAYMENT.ORDER,MEPS.CUST** using the above navigation.
2. Authorize the payment.



Authorize Payments




Authorize Payments




Authorize Payments




Authorize Payments

3. Run the service and the payment moves to status 999.
4. Outward pacs008 file will be generated in **DEOutwardInteg** folder, after running the **BNK/INTEGRATION.SERVICE**. [SFD-BNK24137HDKDG0DF.xml](../../Resources/Images/Singapore/PPSGMX/Files/SFD-BNK24137HDKDG0DF.xml)
5. Process and Inward xsys.003 in through DEInwardInteg folder.
   [24137F8S5F86402.xml](../../Resources/Images/Singapore/PPSGMX/Files/24137F8S5F86402.xml)
6. RequestRef should contain value of the original Outward payment’s DE.O.HEADER-Carrier Sequence Number and TPInfo contains reason code.



   DE.O.HEADER



   DE.O.HEADER
7. Launch the **User Menu >Payments>Payments Hub>Payments Inquiries> Received Message-List**.
8. On running **BNK/PAYMENT.STPFLOW.HEAVY** Original Outward pacs.008 moves to 998 status. Reversal Transaction is created and moved to 999 status.
9. Audit trail of Original Payment is updated.
10. Audit trail of reversal transaction.
11. POR.SUPPLEMENTARY.INFO, POR.TRANSACTION of original payment. [POR.SUPPLEMENTARY.INFO S BNK24137HDKDG0DF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137HDKDG0DF.pdf)
    [POR.SUPPLEMENTARY.INFO S BNK241370HBBDBLB.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK241370HBBDBLB.pdf)
12. POR.SUPPLEMENTARY.INFO, POR.TRANSACTION of reversal payment.
    [POR.SUPPLEMENTARY.INFO S BNK24137HDKDG0DF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137HDKDG0DF.pdf)
    [POR.TRANSACTION S BNK241370HBBDBLB.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK241370HBBDBLB.pdf)

[Receive and Process the Rejection Notification (xsys.003) Message for outward customer payment Pacs.009](#)

TPH receives and processes the xsys.003 message from the clearing. **PT.RECEIVEDFILEDETAILS** – file is updated as **MAPPED**. The system maps the xsys.003 for processing using clearing framework.

The process of matching OriginalTransactionIdentification is as follows:

- TPH matches the Request Reference field of xsys.003 message with **CARRIER.SEQ.NO** field in **DE.O.HEADER** table and then find the relevant FT number.
- The corresponding FT number should then match with **OriginalTransactionIdentification** value.
- The reject reason code is configured for Straight Through Processing, system automatically reverses the accounting entries.
- TPH updates the status of the underlying customer payment transaction to 998 (Completed and reversed (payment rejected)).
- TPH updates the audit trail of the underlying customer payment transaction with reason/description of rejection
- Reversal Transaction is created and moved to 999 status.

An example is provided below.

**User Menu>> Payments>>Payment Hub>> Initiate Payment Transaction>Singapore> Initiate MEPS Bank Transfer**

1. Initiate a pacs.009 payment from version PAYMENT.ORDER,MEPS.BANK using the above navigation.
2. Authorize the payment.
3. Run the service and the payment moves to status 999.
4. On running **BNK/INTEGRATION.SERVICE** service, the outward file will be generated in **DEOutwardInteg** folder. [SFD-BNK24137FB00CHLF.xml](../../Resources/Images/Singapore/PPSGMX/Files/SFD-BNK24137FB00CHLF.xml)
5. Process and Inward xsys.003 in through **DEInwardInteg** folder. [24137F8S5F86402 - 71.xml](../../Resources/Images/Singapore/PPSGMX/Files/24137F8S5F86402 - 71.xml)
6. **RequestRef** should contain value of the original Outward payment’s DE.O.HEADER-Carrier Sequence Number and TPInfo contains reason code.



   DE.O.HEADER



   DE.O.HEADER
7. Launch the **User Menu >Payments>Payments Hub>Payments Inquiries> Received Message-List**.
8. On running **BNK/PAYMENT.STPFLOW.HEAVY** Original Outward pacs.008 moves to 998 status. Reversal Transaction is created and moved to 999 status.
9. Audit trail of original payment is updated.
10. Audit trail of reversal transaction.
11. POR.SUPPLEMENTARY.INFO, POR.TRANSACTION of original payment. [POR.SUPPLEMENTARY.INFO S BNK24137FB00CHLF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137FB00CHLF.pdf)
    [POR.TRANSACTION S BNK24137FB00CHLF.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK24137FB00CHLF.pdf)
12. POR.SUPPLEMENTARY.INFO, POR.TRANSACTION of reversal payment. [POR.SUPPLEMENTARY.INFO S BNK24137JBKLB0G0.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.SUPPLEMENTARY.INFO S BNK24137JBKLB0G0.pdf)
    [POR.TRANSACTION S BNK24137JBKLB0G0.pdf](../../Resources/Images/Singapore/PPSGMX/Files/POR.TRANSACTION S BNK24137JBKLB0G0.pdf)

In this topic

- [Working with SGMEPS in ISO20022 (MX)](#WorkingwithSGMEPSinISO20022MX)

- [Understanding of Outward Customer Credit Transfer](#UnderstandingofOutwardCustomerCreditTransfer)
- [Outward Financial Institution Credit Transfer Cover](#OutwardFinancialInstitutionCreditTransferCover)
- [Inward camt.029, Rejection Notification xsys.003, and Authorization Notification xsys.002](#Inwardcamt029RejectionNotificationxsys003andAuthorizationNotificationxsys002)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:08:20 PM IST