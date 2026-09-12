#
# MSXML2.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sun May  3 00:56:43 2026
# Generated from ICL: MSXML2.icl
#
# Additional info:
# TLB2ICL Generator
# Generated from TLB: C:\Windows\System32\msxml3.dll
#

from win.com.autointerfacedef import *

SXH_PROXY_SET_DEFAULT = 0
SXH_PROXY_SET_PRECONFIG = 0
SXH_PROXY_SET_DIRECT = 1
SXH_PROXY_SET_PROXY = 2
SXH_PROXY_SETTING = INT

SXH_SERVER_CERT_IGNORE_UNKNOWN_CA = 256
SXH_SERVER_CERT_IGNORE_WRONG_USAGE = 512
SXH_SERVER_CERT_IGNORE_CERT_CN_INVALID = 4096
SXH_SERVER_CERT_IGNORE_CERT_DATE_INVALID = 8192
SXH_SERVER_CERT_IGNORE_ALL_SERVER_ERRORS = 13056
SXH_SERVER_CERT_OPTION = INT

SXH_OPTION_URL = -1
SXH_OPTION_URL_CODEPAGE = 0
SXH_OPTION_ESCAPE_PERCENT_IN_URL = 1
SXH_OPTION_IGNORE_SERVER_SSL_CERT_ERROR_FLAGS = 2
SXH_OPTION_SELECT_CLIENT_SSL_CERT = 3
SERVERXMLHTTP_OPTION = INT

XMLELEMTYPE_ELEMENT = 0
XMLELEMTYPE_TEXT = 1
XMLELEMTYPE_COMMENT = 2
XMLELEMTYPE_DOCUMENT = 3
XMLELEMTYPE_DTD = 4
XMLELEMTYPE_PI = 5
XMLELEMTYPE_OTHER = 6
tagXMLEMEM_TYPE = INT

@CStructure.make
class _xml_error(CStructure):
    _nLine: IUint
    _pchBuf: BSTR
    _cchBuf: IUint
    _ich: IUint
    _pszFound: BSTR
    _pszExpected: BSTR
    _reserved1: IUlong
    _reserved2: IUlong

SCHEMAUSE_OPTIONAL = 0
SCHEMAUSE_PROHIBITED = 1
SCHEMAUSE_REQUIRED = 2
_SCHEMAUSE = INT

SCHEMACONTENTTYPE_EMPTY = 0
SCHEMACONTENTTYPE_TEXTONLY = 1
SCHEMACONTENTTYPE_ELEMENTONLY = 2
SCHEMACONTENTTYPE_MIXED = 3
_SCHEMACONTENTTYPE = INT

SCHEMAPROCESSCONTENTS_NONE = 0
SCHEMAPROCESSCONTENTS_SKIP = 1
SCHEMAPROCESSCONTENTS_LAX = 2
SCHEMAPROCESSCONTENTS_STRICT = 3
_SCHEMAPROCESSCONTENTS = INT

SCHEMAWHITESPACE_NONE = -1
SCHEMAWHITESPACE_PRESERVE = 0
SCHEMAWHITESPACE_REPLACE = 1
SCHEMAWHITESPACE_COLLAPSE = 2
_SCHEMAWHITESPACE = INT

SCHEMATYPEVARIETY_NONE = -1
SCHEMATYPEVARIETY_ATOMIC = 0
SCHEMATYPEVARIETY_LIST = 1
SCHEMATYPEVARIETY_UNION = 2
_SCHEMATYPEVARIETY = INT

SCHEMADERIVATIONMETHOD_EMPTY = 0
SCHEMADERIVATIONMETHOD_SUBSTITUTION = 1
SCHEMADERIVATIONMETHOD_EXTENSION = 2
SCHEMADERIVATIONMETHOD_RESTRICTION = 4
SCHEMADERIVATIONMETHOD_LIST = 8
SCHEMADERIVATIONMETHOD_UNION = 16
SCHEMADERIVATIONMETHOD_ALL = 255
SCHEMADERIVATIONMETHOD_NONE = 256
_SCHEMADERIVATIONMETHOD = INT

SOMITEM_SCHEMA = 4096
SOMITEM_ATTRIBUTE = 4097
SOMITEM_ATTRIBUTEGROUP = 4098
SOMITEM_NOTATION = 4099
SOMITEM_ANNOTATION = 4100
SOMITEM_IDENTITYCONSTRAINT = 4352
SOMITEM_KEY = 4353
SOMITEM_KEYREF = 4354
SOMITEM_UNIQUE = 4355
SOMITEM_ANYTYPE = 8192
SOMITEM_DATATYPE = 8448
SOMITEM_DATATYPE_ANYTYPE = 8449
SOMITEM_DATATYPE_ANYURI = 8450
SOMITEM_DATATYPE_BASE64BINARY = 8451
SOMITEM_DATATYPE_BOOLEAN = 8452
SOMITEM_DATATYPE_BYTE = 8453
SOMITEM_DATATYPE_DATE = 8454
SOMITEM_DATATYPE_DATETIME = 8455
SOMITEM_DATATYPE_DAY = 8456
SOMITEM_DATATYPE_DECIMAL = 8457
SOMITEM_DATATYPE_DOUBLE = 8458
SOMITEM_DATATYPE_DURATION = 8459
SOMITEM_DATATYPE_ENTITIES = 8460
SOMITEM_DATATYPE_ENTITY = 8461
SOMITEM_DATATYPE_FLOAT = 8462
SOMITEM_DATATYPE_HEXBINARY = 8463
SOMITEM_DATATYPE_ID = 8464
SOMITEM_DATATYPE_IDREF = 8465
SOMITEM_DATATYPE_IDREFS = 8466
SOMITEM_DATATYPE_INT = 8467
SOMITEM_DATATYPE_INTEGER = 8468
SOMITEM_DATATYPE_LANGUAGE = 8469
SOMITEM_DATATYPE_LONG = 8470
SOMITEM_DATATYPE_MONTH = 8471
SOMITEM_DATATYPE_MONTHDAY = 8472
SOMITEM_DATATYPE_NAME = 8473
SOMITEM_DATATYPE_NCNAME = 8474
SOMITEM_DATATYPE_NEGATIVEINTEGER = 8475
SOMITEM_DATATYPE_NMTOKEN = 8476
SOMITEM_DATATYPE_NMTOKENS = 8477
SOMITEM_DATATYPE_NONNEGATIVEINTEGER = 8478
SOMITEM_DATATYPE_NONPOSITIVEINTEGER = 8479
SOMITEM_DATATYPE_NORMALIZEDSTRING = 8480
SOMITEM_DATATYPE_NOTATION = 8481
SOMITEM_DATATYPE_POSITIVEINTEGER = 8482
SOMITEM_DATATYPE_QNAME = 8483
SOMITEM_DATATYPE_SHORT = 8484
SOMITEM_DATATYPE_STRING = 8485
SOMITEM_DATATYPE_TIME = 8486
SOMITEM_DATATYPE_TOKEN = 8487
SOMITEM_DATATYPE_UNSIGNEDBYTE = 8488
SOMITEM_DATATYPE_UNSIGNEDINT = 8489
SOMITEM_DATATYPE_UNSIGNEDLONG = 8490
SOMITEM_DATATYPE_UNSIGNEDSHORT = 8491
SOMITEM_DATATYPE_YEAR = 8492
SOMITEM_DATATYPE_YEARMONTH = 8493
SOMITEM_DATATYPE_ANYSIMPLETYPE = 8703
SOMITEM_SIMPLETYPE = 8704
SOMITEM_COMPLEXTYPE = 9216
SOMITEM_PARTICLE = 16384
SOMITEM_ANY = 16385
SOMITEM_ANYATTRIBUTE = 16386
SOMITEM_ELEMENT = 16387
SOMITEM_GROUP = 16640
SOMITEM_ALL = 16641
SOMITEM_CHOICE = 16642
SOMITEM_SEQUENCE = 16643
SOMITEM_EMPTYPARTICLE = 16644
SOMITEM_NULL = 2048
SOMITEM_NULL_TYPE = 10240
SOMITEM_NULL_ANY = 18433
SOMITEM_NULL_ANYATTRIBUTE = 18434
SOMITEM_NULL_ELEMENT = 18435
_SOMITEMTYPE = INT

NODE_INVALID = 0
NODE_ELEMENT = 1
NODE_ATTRIBUTE = 2
NODE_TEXT = 3
NODE_CDATA_SECTION = 4
NODE_ENTITY_REFERENCE = 5
NODE_ENTITY = 6
NODE_PROCESSING_INSTRUCTION = 7
NODE_COMMENT = 8
NODE_DOCUMENT = 9
NODE_DOCUMENT_TYPE = 10
NODE_DOCUMENT_FRAGMENT = 11
NODE_NOTATION = 12
tagDOMNodeType = INT

class IXMLDOMImplementation(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8F-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(BSTR, BSTR, PTR(BOOL))
    def hasFeature(self, feature: BSTR, version: BSTR, pOut: IPointer[BOOL]) -> int: ...

    virtual_table.build()

class IXMLDOMNode(IDispatch):
    """
    Core DOM node interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF80-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(PVOID)
    def get_parentNode(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(PVOID)
    def get_childNodes(self, ppOut: IDoublePtr['IXMLDOMNodeList']) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(PVOID)
    def get_firstChild(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(PVOID)
    def get_lastChild(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(PVOID)
    def get_previousSibling(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(PVOID)
    def get_nextSibling(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(PVOID)
    def get_attributes(self, ppOut: IDoublePtr['IXMLDOMNamedNodeMap']) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PVOID, VARIANT, PVOID)
    def insertBefore(self, newChild: IPointer['IXMLDOMNode'], refChild: VARIANT, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PVOID, PVOID, PVOID)
    def replaceChild(self, newChild: IPointer['IXMLDOMNode'], oldChild: IPointer['IXMLDOMNode'], ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PVOID, PVOID)
    def removeChild(self, childNode: IPointer['IXMLDOMNode'], ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PVOID, PVOID)
    def appendChild(self, newChild: IPointer['IXMLDOMNode'], ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_ownerDocument(self, ppOut: IDoublePtr['IXMLDOMDocument']) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, PVOID)
    def cloneNode(self, deep: bool, ppOut: IDoublePtr['IXMLDOMNode']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(PVOID)
    def get_definition(self, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PVOID, PTR(BSTR))
    def transformNode(self, stylesheet: IPointer['IXMLDOMNode'], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, PVOID)
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr['IXMLDOMNodeList']) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, PVOID)
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr['IXMLDOMNode']) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PVOID, VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer['IXMLDOMNode'], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    virtual_table.build()

class IXMLDOMNodeList(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF82-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(LONG, DOUBLE_PTR(IXMLDOMNode))
    def get_item(self, index: int, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        collection of nodes
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of nodes in the collection
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def nextNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        get next node from iterator
        """
    @virtual_table.com_function()
    def reset(self) -> int:
        """
        reset the position of iterator
        """
    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class IXMLDOMNamedNodeMap(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF83-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def getNamedItem(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        lookup item by name
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def setNamedItem(self, newItem: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        set item by name
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def removeNamedItem(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove item by name
        """
    @virtual_table.com_function(LONG, DOUBLE_PTR(IXMLDOMNode))
    def get_item(self, index: int, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        collection of nodes
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of nodes in the collection
        """
    @virtual_table.com_function(BSTR, BSTR, DOUBLE_PTR(IXMLDOMNode))
    def getQualifiedItem(self, baseName: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        lookup the item by name and namespace
        """
    @virtual_table.com_function(BSTR, BSTR, DOUBLE_PTR(IXMLDOMNode))
    def removeQualifiedItem(self, baseName: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove the item by name and namespace
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def nextNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        get next node from iterator
        """
    @virtual_table.com_function()
    def reset(self) -> int:
        """
        reset the position of iterator
        """
    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class IXMLDOMDocument(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF81-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_ownerDocument(self, ppOut: IDoublePtr['IXMLDOMDocument']) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PVOID)
    def get_doctype(self, ppOut: IDoublePtr['IXMLDOMDocumentType']) -> int:
        """
        node corresponding to the DOCTYPE
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMImplementation))
    def get_implementation(self, ppOut: IDoublePtr[IXMLDOMImplementation]) -> int:
        """
        info on this DOM implementation
        """
    @virtual_table.com_function(PVOID)
    def get_documentElement(self, ppOut: IDoublePtr['IXMLDOMElement']) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(PVOID)
    def documentElement(self, param0: IPointer['IXMLDOMElement']) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createElement(self, tagName: BSTR, ppOut: IDoublePtr['IXMLDOMElement']) -> int:
        """
        create an Element node
        """
    @virtual_table.com_function(PVOID)
    def createDocumentFragment(self, ppOut: IDoublePtr['IXMLDOMDocumentFragment']) -> int:
        """
        create a DocumentFragment node
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createTextNode(self, data: BSTR, ppOut: IDoublePtr['IXMLDOMText']) -> int:
        """
        create a text node
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createComment(self, data: BSTR, ppOut: IDoublePtr['IXMLDOMComment']) -> int:
        """
        create a comment node
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createCDATASection(self, data: BSTR, ppOut: IDoublePtr['IXMLDOMCDATASection']) -> int:
        """
        create a CDATA section node
        """
    @virtual_table.com_function(BSTR, BSTR, PVOID)
    def createProcessingInstruction(self, target: BSTR, data: BSTR, ppOut: IDoublePtr['IXMLDOMProcessingInstruction']) -> int:
        """
        create a processing instruction node
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createAttribute(self, name: BSTR, ppOut: IDoublePtr['IXMLDOMAttribute']) -> int:
        """
        create an attribute node
        """
    @virtual_table.com_function(BSTR, PVOID)
    def createEntityReference(self, name: BSTR, ppOut: IDoublePtr['IXMLDOMEntityReference']) -> int:
        """
        create an entity reference node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def getElementsByTagName(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        build a list of elements by name
        """
    @virtual_table.com_function(VARIANT, BSTR, BSTR, DOUBLE_PTR(IXMLDOMNode))
    def createNode(self, type: VARIANT, name: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        create a node of the specified node type and name
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def nodeFromID(self, idString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        retrieve node from it's ID
        """
    @virtual_table.com_function(VARIANT, PTR(BOOL))
    def load(self, xmlSource: VARIANT, pOut: IPointer[BOOL]) -> int:
        """
        load document from the specified XML source
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        get the state of the XML document
        """
    @virtual_table.com_function(PVOID)
    def get_parseError(self, ppOut: IDoublePtr['IXMLDOMParseError']) -> int:
        """
        get the last parser error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        get the URL for the loaded XML document
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_async(self, pOut: IPointer[BOOL]) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function(BOOL)
    def put_async(self, param0: bool) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        abort an asynchronous download
        """
    @virtual_table.com_function(BSTR, PTR(BOOL))
    def loadXML(self, bstrXML: BSTR, pOut: IPointer[BOOL]) -> int:
        """
        load the document from a string
        """
    @virtual_table.com_function(VARIANT)
    def save(self, destination: VARIANT) -> int:
        """
        save the document to a specified destination
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_validateOnParse(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(BOOL)
    def put_validateOnParse(self, param0: bool) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_resolveExternals(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(BOOL)
    def put_resolveExternals(self, param0: bool) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_preserveWhiteSpace(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(BOOL)
    def put_preserveWhiteSpace(self, param0: bool) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(VARIANT)
    def put_onreadystatechange(self, param0: VARIANT) -> int:
        """
        register a readystatechange event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ondataavailable(self, param0: VARIANT) -> int:
        """
        register an ondataavailable event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ontransformnode(self, param0: VARIANT) -> int:
        """
        register an ontransformnode event handler
        """
    virtual_table.build()

class IXMLDOMDocumentType(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8B-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the document type (root of the tree)
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_entities(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        a list of entities in the document
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_notations(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        a list of notations in the document
        """
    virtual_table.build()

class IXMLDOMElement(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF86-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_tagName(self, pOut: IPointer[BSTR]) -> int:
        """
        get the tagName of the element
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getAttribute(self, name: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        look up the string value of an attribute by name
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setAttribute(self, name: BSTR, value: VARIANT) -> int:
        """
        set the string value of an attribute by name
        """
    @virtual_table.com_function(BSTR)
    def removeAttribute(self, name: BSTR) -> int:
        """
        remove an attribute by name
        """
    @virtual_table.com_function(BSTR, PVOID)
    def getAttributeNode(self, name: BSTR, ppOut: IDoublePtr['IXMLDOMAttribute']) -> int:
        """
        look up the attribute node by name
        """
    @virtual_table.com_function(PVOID, PVOID)
    def setAttributeNode(self, DOMAttribute: IPointer['IXMLDOMAttribute'], ppOut: IDoublePtr['IXMLDOMAttribute']) -> int:
        """
        set the specified attribute on the element
        """
    @virtual_table.com_function(PVOID, PVOID)
    def removeAttributeNode(self, DOMAttribute: IPointer['IXMLDOMAttribute'], ppOut: IDoublePtr['IXMLDOMAttribute']) -> int:
        """
        remove the specified attribute
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def getElementsByTagName(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        build a list of elements by name
        """
    @virtual_table.com_function()
    def normalize(self) -> int:
        """
        collapse all adjacent text nodes in sub-tree
        """
    virtual_table.build()

class IXMLDOMAttribute(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF85-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int:
        """
        get name of the attribute
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_value(self, pOut: IPointer[VARIANT]) -> int:
        """
        string value of the attribute
        """
    @virtual_table.com_function(VARIANT)
    def put_value(self, param0: VARIANT) -> int:
        """
        string value of the attribute
        """
    virtual_table.build()

class IXMLDOMDocumentFragment(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3EFAA413-272F-11D2-836F-0000F87A7782}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    virtual_table.build()

class IXMLDOMText(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF87-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_data(self, pOut: IPointer[BSTR]) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(BSTR)
    def put_data(self, param0: BSTR) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of characters in value
        """
    @virtual_table.com_function(LONG, LONG, PTR(BSTR))
    def substringData(self, offset: int, count: int, pOut: IPointer[BSTR]) -> int:
        """
        retrieve substring of value
        """
    @virtual_table.com_function(BSTR)
    def appendData(self, data: BSTR) -> int:
        """
        append string to value
        """
    @virtual_table.com_function(LONG, BSTR)
    def insertData(self, offset: int, data: BSTR) -> int:
        """
        insert string into value
        """
    @virtual_table.com_function(LONG, LONG)
    def deleteData(self, offset: int, count: int) -> int:
        """
        delete string within the value
        """
    @virtual_table.com_function(LONG, LONG, BSTR)
    def replaceData(self, offset: int, count: int, data: BSTR) -> int:
        """
        replace string within the value
        """
    @virtual_table.com_function(LONG, PVOID)
    def splitText(self, offset: int, ppOut: IDoublePtr['IXMLDOMText']) -> int:
        """
        split the text node into two text nodes at the position specified
        """
    virtual_table.build()

class IXMLDOMCharacterData(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF84-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_data(self, pOut: IPointer[BSTR]) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(BSTR)
    def put_data(self, param0: BSTR) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of characters in value
        """
    @virtual_table.com_function(LONG, LONG, PTR(BSTR))
    def substringData(self, offset: int, count: int, pOut: IPointer[BSTR]) -> int:
        """
        retrieve substring of value
        """
    @virtual_table.com_function(BSTR)
    def appendData(self, data: BSTR) -> int:
        """
        append string to value
        """
    @virtual_table.com_function(LONG, BSTR)
    def insertData(self, offset: int, data: BSTR) -> int:
        """
        insert string into value
        """
    @virtual_table.com_function(LONG, LONG)
    def deleteData(self, offset: int, count: int) -> int:
        """
        delete string within the value
        """
    @virtual_table.com_function(LONG, LONG, BSTR)
    def replaceData(self, offset: int, count: int, data: BSTR) -> int:
        """
        replace string within the value
        """
    virtual_table.build()

class IXMLDOMComment(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF88-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_data(self, pOut: IPointer[BSTR]) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(BSTR)
    def put_data(self, param0: BSTR) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of characters in value
        """
    @virtual_table.com_function(LONG, LONG, PTR(BSTR))
    def substringData(self, offset: int, count: int, pOut: IPointer[BSTR]) -> int:
        """
        retrieve substring of value
        """
    @virtual_table.com_function(BSTR)
    def appendData(self, data: BSTR) -> int:
        """
        append string to value
        """
    @virtual_table.com_function(LONG, BSTR)
    def insertData(self, offset: int, data: BSTR) -> int:
        """
        insert string into value
        """
    @virtual_table.com_function(LONG, LONG)
    def deleteData(self, offset: int, count: int) -> int:
        """
        delete string within the value
        """
    @virtual_table.com_function(LONG, LONG, BSTR)
    def replaceData(self, offset: int, count: int, data: BSTR) -> int:
        """
        replace string within the value
        """
    virtual_table.build()

class IXMLDOMCDATASection(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8A-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_data(self, pOut: IPointer[BSTR]) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(BSTR)
    def put_data(self, param0: BSTR) -> int:
        """
        value of the node
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of characters in value
        """
    @virtual_table.com_function(LONG, LONG, PTR(BSTR))
    def substringData(self, offset: int, count: int, pOut: IPointer[BSTR]) -> int:
        """
        retrieve substring of value
        """
    @virtual_table.com_function(BSTR)
    def appendData(self, data: BSTR) -> int:
        """
        append string to value
        """
    @virtual_table.com_function(LONG, BSTR)
    def insertData(self, offset: int, data: BSTR) -> int:
        """
        insert string into value
        """
    @virtual_table.com_function(LONG, LONG)
    def deleteData(self, offset: int, count: int) -> int:
        """
        delete string within the value
        """
    @virtual_table.com_function(LONG, LONG, BSTR)
    def replaceData(self, offset: int, count: int, data: BSTR) -> int:
        """
        replace string within the value
        """
    @virtual_table.com_function(LONG, DOUBLE_PTR(IXMLDOMText))
    def splitText(self, offset: int, ppOut: IDoublePtr[IXMLDOMText]) -> int:
        """
        split the text node into two text nodes at the position specified
        """
    virtual_table.build()

class IXMLDOMProcessingInstruction(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF89-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_target(self, pOut: IPointer[BSTR]) -> int:
        """
        the target
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_data(self, pOut: IPointer[BSTR]) -> int:
        """
        the data
        """
    @virtual_table.com_function(BSTR)
    def put_data(self, param0: BSTR) -> int:
        """
        the data
        """
    virtual_table.build()

class IXMLDOMEntityReference(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8E-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    virtual_table.build()

class IXMLDOMParseError(IDispatch):
    """
    structure for reporting parser errors
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3EFAA426-272F-11D2-836F-0000F87A7782}")

    @virtual_table.com_function(PLONG)
    def get_errorCode(self, pOut: IPointer[LONG]) -> int:
        """
        the error code
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        the URL of the XML document containing the error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_reason(self, pOut: IPointer[BSTR]) -> int:
        """
        the cause of the error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_srcText(self, pOut: IPointer[BSTR]) -> int:
        """
        the data where the error occurred
        """
    @virtual_table.com_function(PLONG)
    def get_line(self, pOut: IPointer[LONG]) -> int:
        """
        the line number in the XML document where the error occurred
        """
    @virtual_table.com_function(PLONG)
    def get_linepos(self, pOut: IPointer[LONG]) -> int:
        """
        the character position in the line containing the error
        """
    @virtual_table.com_function(PLONG)
    def get_filepos(self, pOut: IPointer[LONG]) -> int:
        """
        the absolute file position in the XML document containing the error
        """
    virtual_table.build()

class IXMLDOMDocument2(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF95-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocumentType))
    def get_doctype(self, ppOut: IDoublePtr[IXMLDOMDocumentType]) -> int:
        """
        node corresponding to the DOCTYPE
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMImplementation))
    def get_implementation(self, ppOut: IDoublePtr[IXMLDOMImplementation]) -> int:
        """
        info on this DOM implementation
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMElement))
    def get_documentElement(self, ppOut: IDoublePtr[IXMLDOMElement]) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(PTR(IXMLDOMElement))
    def documentElement(self, param0: IPointer[IXMLDOMElement]) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMElement))
    def createElement(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMElement]) -> int:
        """
        create an Element node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocumentFragment))
    def createDocumentFragment(self, ppOut: IDoublePtr[IXMLDOMDocumentFragment]) -> int:
        """
        create a DocumentFragment node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMText))
    def createTextNode(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMText]) -> int:
        """
        create a text node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMComment))
    def createComment(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMComment]) -> int:
        """
        create a comment node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMCDATASection))
    def createCDATASection(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMCDATASection]) -> int:
        """
        create a CDATA section node
        """
    @virtual_table.com_function(BSTR, BSTR, DOUBLE_PTR(IXMLDOMProcessingInstruction))
    def createProcessingInstruction(self, target: BSTR, data: BSTR, ppOut: IDoublePtr[IXMLDOMProcessingInstruction]) -> int:
        """
        create a processing instruction node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMAttribute))
    def createAttribute(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMAttribute]) -> int:
        """
        create an attribute node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMEntityReference))
    def createEntityReference(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMEntityReference]) -> int:
        """
        create an entity reference node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def getElementsByTagName(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        build a list of elements by name
        """
    @virtual_table.com_function(VARIANT, BSTR, BSTR, DOUBLE_PTR(IXMLDOMNode))
    def createNode(self, type: VARIANT, name: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        create a node of the specified node type and name
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def nodeFromID(self, idString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        retrieve node from it's ID
        """
    @virtual_table.com_function(VARIANT, PTR(BOOL))
    def load(self, xmlSource: VARIANT, pOut: IPointer[BOOL]) -> int:
        """
        load document from the specified XML source
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        get the state of the XML document
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMParseError))
    def get_parseError(self, ppOut: IDoublePtr[IXMLDOMParseError]) -> int:
        """
        get the last parser error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        get the URL for the loaded XML document
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_async(self, pOut: IPointer[BOOL]) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function(BOOL)
    def put_async(self, param0: bool) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        abort an asynchronous download
        """
    @virtual_table.com_function(BSTR, PTR(BOOL))
    def loadXML(self, bstrXML: BSTR, pOut: IPointer[BOOL]) -> int:
        """
        load the document from a string
        """
    @virtual_table.com_function(VARIANT)
    def save(self, destination: VARIANT) -> int:
        """
        save the document to a specified destination
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_validateOnParse(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(BOOL)
    def put_validateOnParse(self, param0: bool) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_resolveExternals(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(BOOL)
    def put_resolveExternals(self, param0: bool) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_preserveWhiteSpace(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(BOOL)
    def put_preserveWhiteSpace(self, param0: bool) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(VARIANT)
    def put_onreadystatechange(self, param0: VARIANT) -> int:
        """
        register a readystatechange event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ondataavailable(self, param0: VARIANT) -> int:
        """
        register an ondataavailable event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ontransformnode(self, param0: VARIANT) -> int:
        """
        register an ontransformnode event handler
        """
    @virtual_table.com_function(PVOID)
    def get_namespaces(self, ppOut: IDoublePtr['IXMLDOMSchemaCollection']) -> int:
        """
        A collection of all namespaces for this document
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_schemas(self, pOut: IPointer[VARIANT]) -> int:
        """
        The associated schema cache
        """
    @virtual_table.com_function(VARIANT)
    def schemas(self, param0: VARIANT) -> int:
        """
        The associated schema cache
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMParseError))
    def validate(self, ppOut: IDoublePtr[IXMLDOMParseError]) -> int:
        """
        perform runtime validation on the currently loaded XML document
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setProperty(self, name: BSTR, value: VARIANT) -> int:
        """
        set the value of the named property
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getProperty(self, name: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        get the value of the named property
        """
    virtual_table.build()

class IXMLDOMSchemaCollection(IDispatch):
    """
    XML Schemas Collection
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{373984C8-B845-449B-91E7-45AC83036ADE}")

    @virtual_table.com_function(BSTR, VARIANT)
    def add(self, namespaceURI: BSTR, var: VARIANT) -> int:
        """
        add a new schema
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def get(self, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        lookup schema by namespaceURI
        """
    @virtual_table.com_function(BSTR)
    def remove(self, namespaceURI: BSTR) -> int:
        """
        remove schema by namespaceURI
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of schemas in collection
        """
    @virtual_table.com_function(LONG, PTR(BSTR))
    def get_namespaceURI(self, index: int, pOut: IPointer[BSTR]) -> int:
        """
        Get namespaceURI for schema by index
        """
    @virtual_table.com_function(PVOID)
    def addCollection(self, otherCollection: IPointer['IXMLDOMSchemaCollection']) -> int:
        """
        copy & merge other collection into this one
        """
    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class IXMLDOMDocument3(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF96-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocumentType))
    def get_doctype(self, ppOut: IDoublePtr[IXMLDOMDocumentType]) -> int:
        """
        node corresponding to the DOCTYPE
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMImplementation))
    def get_implementation(self, ppOut: IDoublePtr[IXMLDOMImplementation]) -> int:
        """
        info on this DOM implementation
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMElement))
    def get_documentElement(self, ppOut: IDoublePtr[IXMLDOMElement]) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(PTR(IXMLDOMElement))
    def documentElement(self, param0: IPointer[IXMLDOMElement]) -> int:
        """
        the root of the tree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMElement))
    def createElement(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMElement]) -> int:
        """
        create an Element node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocumentFragment))
    def createDocumentFragment(self, ppOut: IDoublePtr[IXMLDOMDocumentFragment]) -> int:
        """
        create a DocumentFragment node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMText))
    def createTextNode(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMText]) -> int:
        """
        create a text node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMComment))
    def createComment(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMComment]) -> int:
        """
        create a comment node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMCDATASection))
    def createCDATASection(self, data: BSTR, ppOut: IDoublePtr[IXMLDOMCDATASection]) -> int:
        """
        create a CDATA section node
        """
    @virtual_table.com_function(BSTR, BSTR, DOUBLE_PTR(IXMLDOMProcessingInstruction))
    def createProcessingInstruction(self, target: BSTR, data: BSTR, ppOut: IDoublePtr[IXMLDOMProcessingInstruction]) -> int:
        """
        create a processing instruction node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMAttribute))
    def createAttribute(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMAttribute]) -> int:
        """
        create an attribute node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMEntityReference))
    def createEntityReference(self, name: BSTR, ppOut: IDoublePtr[IXMLDOMEntityReference]) -> int:
        """
        create an entity reference node
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def getElementsByTagName(self, tagName: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        build a list of elements by name
        """
    @virtual_table.com_function(VARIANT, BSTR, BSTR, DOUBLE_PTR(IXMLDOMNode))
    def createNode(self, type: VARIANT, name: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        create a node of the specified node type and name
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def nodeFromID(self, idString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        retrieve node from it's ID
        """
    @virtual_table.com_function(VARIANT, PTR(BOOL))
    def load(self, xmlSource: VARIANT, pOut: IPointer[BOOL]) -> int:
        """
        load document from the specified XML source
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        get the state of the XML document
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMParseError))
    def get_parseError(self, ppOut: IDoublePtr[IXMLDOMParseError]) -> int:
        """
        get the last parser error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        get the URL for the loaded XML document
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_async(self, pOut: IPointer[BOOL]) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function(BOOL)
    def put_async(self, param0: bool) -> int:
        """
        flag for asynchronous download
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        abort an asynchronous download
        """
    @virtual_table.com_function(BSTR, PTR(BOOL))
    def loadXML(self, bstrXML: BSTR, pOut: IPointer[BOOL]) -> int:
        """
        load the document from a string
        """
    @virtual_table.com_function(VARIANT)
    def save(self, destination: VARIANT) -> int:
        """
        save the document to a specified destination
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_validateOnParse(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(BOOL)
    def put_validateOnParse(self, param0: bool) -> int:
        """
        indicates whether the parser performs validation
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_resolveExternals(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(BOOL)
    def put_resolveExternals(self, param0: bool) -> int:
        """
        indicates whether the parser resolves references to external DTD/Entities/Schema
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_preserveWhiteSpace(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(BOOL)
    def put_preserveWhiteSpace(self, param0: bool) -> int:
        """
        indicates whether the parser preserves whitespace
        """
    @virtual_table.com_function(VARIANT)
    def put_onreadystatechange(self, param0: VARIANT) -> int:
        """
        register a readystatechange event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ondataavailable(self, param0: VARIANT) -> int:
        """
        register an ondataavailable event handler
        """
    @virtual_table.com_function(VARIANT)
    def put_ontransformnode(self, param0: VARIANT) -> int:
        """
        register an ontransformnode event handler
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMSchemaCollection))
    def get_namespaces(self, ppOut: IDoublePtr[IXMLDOMSchemaCollection]) -> int:
        """
        A collection of all namespaces for this document
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_schemas(self, pOut: IPointer[VARIANT]) -> int:
        """
        The associated schema cache
        """
    @virtual_table.com_function(VARIANT)
    def schemas(self, param0: VARIANT) -> int:
        """
        The associated schema cache
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMParseError))
    def validate(self, ppOut: IDoublePtr[IXMLDOMParseError]) -> int:
        """
        perform runtime validation on the currently loaded XML document
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setProperty(self, name: BSTR, value: VARIANT) -> int:
        """
        set the value of the named property
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getProperty(self, name: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        get the value of the named property
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMParseError))
    def validateNode(self, node: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMParseError]) -> int:
        """
        perform runtime validation on the currently loaded XML document node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), BOOL, DOUBLE_PTR(IXMLDOMNode))
    def importNode(self, node: IPointer[IXMLDOMNode], deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        clone node such that clones ownerDocument is this document
        """
    virtual_table.build()

class IXMLDOMNotation(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8C-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_publicId(self, pOut: IPointer[VARIANT]) -> int:
        """
        the public ID
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_systemId(self, pOut: IPointer[VARIANT]) -> int:
        """
        the system ID
        """
    virtual_table.build()

class IXMLDOMEntity(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF8D-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_publicId(self, pOut: IPointer[VARIANT]) -> int:
        """
        the public ID
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_systemId(self, pOut: IPointer[VARIANT]) -> int:
        """
        the system ID
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_notationName(self, pOut: IPointer[BSTR]) -> int:
        """
        the name of the notation
        """
    virtual_table.build()

class IXMLDOMParseError2(IDispatch):
    """
    structure for reporting parser errors
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3EFAA428-272F-11D2-836F-0000F87A7782}")

    @virtual_table.com_function(PLONG)
    def get_errorCode(self, pOut: IPointer[LONG]) -> int:
        """
        the error code
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        the URL of the XML document containing the error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_reason(self, pOut: IPointer[BSTR]) -> int:
        """
        the cause of the error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_srcText(self, pOut: IPointer[BSTR]) -> int:
        """
        the data where the error occurred
        """
    @virtual_table.com_function(PLONG)
    def get_line(self, pOut: IPointer[LONG]) -> int:
        """
        the line number in the XML document where the error occurred
        """
    @virtual_table.com_function(PLONG)
    def get_linepos(self, pOut: IPointer[LONG]) -> int:
        """
        the character position in the line containing the error
        """
    @virtual_table.com_function(PLONG)
    def get_filepos(self, pOut: IPointer[LONG]) -> int:
        """
        the absolute file position in the XML document containing the error
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_errorXPath(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_allErrors(self, ppOut: IDoublePtr['IXMLDOMParseErrorCollection']) -> int: ...

    @virtual_table.com_function(LONG, PTR(BSTR))
    def errorParameters(self, index: int, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_errorParametersCount(self, pOut: IPointer[LONG]) -> int: ...

    virtual_table.build()

class IXMLDOMParseErrorCollection(IDispatch):
    """
    structure for reporting parser errors
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3EFAA429-272F-11D2-836F-0000F87A7782}")

    @virtual_table.com_function(LONG, DOUBLE_PTR(IXMLDOMParseError2))
    def get_item(self, index: int, ppOut: IDoublePtr[IXMLDOMParseError2]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMParseError2))
    def get_next(self, ppOut: IDoublePtr[IXMLDOMParseError2]) -> int: ...

    @virtual_table.com_function()
    def reset(self) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class IXTLRuntime(IDispatch):
    """
    XTL runtime object
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3EFAA425-272F-11D2-836F-0000F87A7782}")

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeName(self, pOut: IPointer[BSTR]) -> int:
        """
        name of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeValue(self, param0: VARIANT) -> int:
        """
        value stored in the node
        """
    @virtual_table.com_function(PVOID)
    def get_nodeType(self, pOut: IPointer['DOMNodeType']) -> int:
        """
        the node's type
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_parentNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        parent of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNodeList))
    def get_childNodes(self, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        the collection of the node's children
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_firstChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        first child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_lastChild(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        last child of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_previousSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        left sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_nextSibling(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        right sibling of the node
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNamedNodeMap))
    def get_attributes(self, ppOut: IDoublePtr[IXMLDOMNamedNodeMap]) -> int:
        """
        the collection of the node's attributes
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT, DOUBLE_PTR(IXMLDOMNode))
    def insertBefore(self, newChild: IPointer[IXMLDOMNode], refChild: VARIANT, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        insert a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def replaceChild(self, newChild: IPointer[IXMLDOMNode], oldChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        replace a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def removeChild(self, childNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        remove a child node
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def appendChild(self, newChild: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        append a child node
        """
    @virtual_table.com_function(PTR(BOOL))
    def hasChildNodes(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_ownerDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int:
        """
        document that contains the node
        """
    @virtual_table.com_function(BOOL, DOUBLE_PTR(IXMLDOMNode))
    def cloneNode(self, deep: bool, ppOut: IDoublePtr[IXMLDOMNode]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_nodeTypeString(self, pOut: IPointer[BSTR]) -> int:
        """
        the type of node in string form
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        text content of the node and subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_specified(self, pOut: IPointer[BOOL]) -> int:
        """
        indicates whether node is a default value
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_definition(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        pointer to the definition of the node in the DTD or schema
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_nodeTypedValue(self, pOut: IPointer[VARIANT]) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(VARIANT)
    def put_nodeTypedValue(self, param0: VARIANT) -> int:
        """
        get the strongly typed value of the node
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_dataType(self, pOut: IPointer[VARIANT]) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(BSTR)
    def put_dataType(self, param0: BSTR) -> int:
        """
        the data type of the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_xml(self, pOut: IPointer[BSTR]) -> int:
        """
        return the XML source for the node and each of its descendants
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PTR(BSTR))
    def transformNode(self, stylesheet: IPointer[IXMLDOMNode], pOut: IPointer[BSTR]) -> int:
        """
        apply the stylesheet to the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNodeList))
    def selectNodes(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNodeList]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def selectSingleNode(self, queryString: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        execute query on the subtree
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_parsed(self, pOut: IPointer[BOOL]) -> int:
        """
        has sub-tree been completely parsed
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int:
        """
        the URI for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_prefix(self, pOut: IPointer[BSTR]) -> int:
        """
        the prefix for the namespace applying to the node
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseName(self, pOut: IPointer[BSTR]) -> int:
        """
        the base name of the node (nodename with the prefix stripped off)
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), VARIANT)
    def transformNodeToObject(self, stylesheet: IPointer[IXMLDOMNode], outputObject: VARIANT) -> int:
        """
        apply the stylesheet to the subtree, returning the result through a document or a stream
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), PLONG)
    def uniqueID(self, pNode: IPointer[IXMLDOMNode], pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), PLONG)
    def depth(self, pNode: IPointer[IXMLDOMNode], pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), PLONG)
    def childNumber(self, pNode: IPointer[IXMLDOMNode], pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(BSTR, PTR(IXMLDOMNode), PLONG)
    def ancestorChildNumber(self, bstrNodeName: BSTR, pNode: IPointer[IXMLDOMNode], pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), PLONG)
    def absoluteChildNumber(self, pNode: IPointer[IXMLDOMNode], pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(LONG, BSTR, PTR(BSTR))
    def formatIndex(self, lIndex: int, bstrFormat: BSTR, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE, BSTR, PTR(BSTR))
    def formatNumber(self, dblNumber: DOUBLE, bstrFormat: BSTR, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(VARIANT, BSTR, VARIANT, PTR(BSTR))
    def formatDate(self, varDate: VARIANT, bstrFormat: BSTR, varDestLocale: VARIANT, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(VARIANT, BSTR, VARIANT, PTR(BSTR))
    def formatTime(self, varTime: VARIANT, bstrFormat: BSTR, varDestLocale: VARIANT, pOut: IPointer[BSTR]) -> int: ...

    virtual_table.build()

class IXSLTemplate(IDispatch):
    """
    IXSLTemplate Interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF93-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(PTR(IXMLDOMNode))
    def stylesheet(self, param0: IPointer[IXMLDOMNode]) -> int:
        """
        stylesheet to use with processors
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_stylesheet(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        stylesheet to use with processors
        """
    @virtual_table.com_function(PVOID)
    def createProcessor(self, ppOut: IDoublePtr['IXSLProcessor']) -> int:
        """
        create a new processor object
        """
    virtual_table.build()

class IXSLProcessor(IDispatch):
    """
    IXSLProcessor Interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2933BF92-7B36-11D2-B20E-00C04F983E60}")

    @virtual_table.com_function(VARIANT)
    def put_input(self, param0: VARIANT) -> int:
        """
        XML input tree to transform
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_input(self, pOut: IPointer[VARIANT]) -> int:
        """
        XML input tree to transform
        """
    @virtual_table.com_function(DOUBLE_PTR(IXSLTemplate))
    def get_ownerTemplate(self, ppOut: IDoublePtr[IXSLTemplate]) -> int:
        """
        template object used to create this processor object
        """
    @virtual_table.com_function(BSTR, BSTR)
    def setStartMode(self, mode: BSTR, namespaceURI: BSTR) -> int:
        """
        set XSL mode and it's namespace
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_startMode(self, pOut: IPointer[BSTR]) -> int:
        """
        starting XSL mode
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_startModeURI(self, pOut: IPointer[BSTR]) -> int:
        """
        namespace of starting XSL mode
        """
    @virtual_table.com_function(VARIANT)
    def put_output(self, param0: VARIANT) -> int:
        """
        custom stream object for transform output
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_output(self, pOut: IPointer[VARIANT]) -> int:
        """
        custom stream object for transform output
        """
    @virtual_table.com_function(PTR(BOOL))
    def transform(self, pOut: IPointer[BOOL]) -> int:
        """
        start/resume the XSL transformation process
        """
    @virtual_table.com_function()
    def reset(self) -> int:
        """
        reset state of processor and abort current transform
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        current state of the processor
        """
    @virtual_table.com_function(BSTR, VARIANT, BSTR)
    def addParameter(self, baseName: BSTR, parameter: VARIANT, namespaceURI: BSTR) -> int:
        """
        set <xsl:param> values
        """
    @virtual_table.com_function(PTR(IDispatch), BSTR)
    def addObject(self, obj: IPointer[IDispatch], namespaceURI: BSTR) -> int:
        """
        pass object to stylesheet
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_stylesheet(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        current stylesheet being used
        """
    virtual_table.build()

class ISAXXMLReader(IUnknown):
    """
    ISAXXMLReader interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{A4F96ED0-F829-476E-81C0-CDC7BD2A0802}")

    @virtual_table.com_function(PWORD, PTR(BOOL))
    def getFeature(self, pwchName: IPointer[WORD], pvfValue: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PWORD, BOOL)
    def putFeature(self, pwchName: IPointer[WORD], vfValue: bool) -> int: ...

    @virtual_table.com_function(PWORD, PTR(VARIANT))
    def getProperty(self, pwchName: IPointer[WORD], pvarValue: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PWORD, VARIANT)
    def putProperty(self, pwchName: IPointer[WORD], varValue: VARIANT) -> int: ...

    @virtual_table.com_function(PVOID)
    def getEntityResolver(self, ppResolver: IDoublePtr['ISAXEntityResolver']) -> int: ...

    @virtual_table.com_function(PVOID)
    def putEntityResolver(self, pResolver: IPointer['ISAXEntityResolver']) -> int: ...

    @virtual_table.com_function(PVOID)
    def getContentHandler(self, ppHandler: IDoublePtr['ISAXContentHandler']) -> int: ...

    @virtual_table.com_function(PVOID)
    def putContentHandler(self, pHandler: IPointer['ISAXContentHandler']) -> int: ...

    @virtual_table.com_function(PVOID)
    def getDTDHandler(self, ppHandler: IDoublePtr['ISAXDTDHandler']) -> int: ...

    @virtual_table.com_function(PVOID)
    def putDTDHandler(self, pHandler: IPointer['ISAXDTDHandler']) -> int: ...

    @virtual_table.com_function(PVOID)
    def getErrorHandler(self, ppHandler: IDoublePtr['ISAXErrorHandler']) -> int: ...

    @virtual_table.com_function(PVOID)
    def putErrorHandler(self, pHandler: IPointer['ISAXErrorHandler']) -> int: ...

    @virtual_table.com_function(PTR(PWORD))
    def getBaseURL(self, ppwchBaseUrl: IDoublePtr[WORD]) -> int: ...

    @virtual_table.com_function(PWORD)
    def putBaseURL(self, pwchBaseUrl: IPointer[WORD]) -> int: ...

    @virtual_table.com_function(PTR(PWORD))
    def getSecureBaseURL(self, ppwchSecureBaseUrl: IDoublePtr[WORD]) -> int: ...

    @virtual_table.com_function(PWORD)
    def putSecureBaseURL(self, pwchSecureBaseUrl: IPointer[WORD]) -> int: ...

    @virtual_table.com_function(VARIANT)
    def parse(self, varInput: VARIANT) -> int: ...

    @virtual_table.com_function(PWORD)
    def parseURL(self, pwchUrl: IPointer[WORD]) -> int: ...

    virtual_table.build()

class ISAXEntityResolver(IUnknown):
    """
    ISAXEntityResolver interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{99BCA7BD-E8C4-4D5F-A0CF-6D907901FF07}")

    @virtual_table.com_function(PWORD, PWORD, PTR(VARIANT))
    def resolveEntity(self, pwchPublicId: IPointer[WORD], pwchSystemId: IPointer[WORD], pvarInput: IPointer[VARIANT]) -> int: ...

    virtual_table.build()

class ISAXContentHandler(IUnknown):
    """
    ISAXContentHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1545CDFA-9E4E-4497-A8A4-2BF7D0112C44}")

    @virtual_table.com_function(PVOID)
    def putDocumentLocator(self, pLocator: IPointer['ISAXLocator']) -> int: ...

    @virtual_table.com_function()
    def startDocument(self) -> int: ...

    @virtual_table.com_function()
    def endDocument(self) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT)
    def startPrefixMapping(self, pwchPrefix: IPointer[WORD], cchPrefix: int, pwchUri: IPointer[WORD], cchUri: int) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def endPrefixMapping(self, pwchPrefix: IPointer[WORD], cchPrefix: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT, PVOID)
    def startElement(self, pwchNamespaceUri: IPointer[WORD], cchNamespaceUri: int, pwchLocalName: IPointer[WORD], cchLocalName: int, pwchQName: IPointer[WORD], cchQName: int, pAttributes: IPointer['ISAXAttributes']) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT)
    def endElement(self, pwchNamespaceUri: IPointer[WORD], cchNamespaceUri: int, pwchLocalName: IPointer[WORD], cchLocalName: int, pwchQName: IPointer[WORD], cchQName: int) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def characters(self, pwchChars: IPointer[WORD], cchChars: int) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def ignorableWhitespace(self, pwchChars: IPointer[WORD], cchChars: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT)
    def processingInstruction(self, pwchTarget: IPointer[WORD], cchTarget: int, pwchData: IPointer[WORD], cchData: int) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def skippedEntity(self, pwchName: IPointer[WORD], cchName: int) -> int: ...

    virtual_table.build()

class ISAXLocator(IUnknown):
    """
    ISAXLocator interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{9B7E472A-0DE4-4640-BFF3-84D38A051C31}")

    @virtual_table.com_function(PINT)
    def getColumnNumber(self, pnColumn: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PINT)
    def getLineNumber(self, pnLine: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PTR(PWORD))
    def getPublicId(self, ppwchPublicId: IDoublePtr[WORD]) -> int: ...

    @virtual_table.com_function(PTR(PWORD))
    def getSystemId(self, ppwchSystemId: IDoublePtr[WORD]) -> int: ...

    virtual_table.build()

class ISAXAttributes(IUnknown):
    """
    ISAXAttributes interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{F078ABE1-45D2-4832-91EA-4466CE2F25C9}")

    @virtual_table.com_function(PINT)
    def getLength(self, pnLength: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT)
    def getURI(self, nIndex: int, ppwchUri: IDoublePtr[WORD], pcchUri: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT)
    def getLocalName(self, nIndex: int, ppwchLocalName: IDoublePtr[WORD], pcchLocalName: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT)
    def getQName(self, nIndex: int, ppwchQName: IDoublePtr[WORD], pcchQName: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT, PTR(PWORD), PINT, PTR(PWORD), PINT)
    def getName(self, nIndex: int, ppwchUri: IDoublePtr[WORD], pcchUri: IPointer[INT], ppwchLocalName: IDoublePtr[WORD], pcchLocalName: IPointer[INT], ppwchQName: IDoublePtr[WORD], pcchQName: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PINT)
    def getIndexFromName(self, pwchUri: IPointer[WORD], cchUri: int, pwchLocalName: IPointer[WORD], cchLocalName: int, pnIndex: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PINT)
    def getIndexFromQName(self, pwchQName: IPointer[WORD], cchQName: int, pnIndex: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT)
    def getType(self, nIndex: int, ppwchType: IDoublePtr[WORD], pcchType: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PTR(PWORD), PINT)
    def getTypeFromName(self, pwchUri: IPointer[WORD], cchUri: int, pwchLocalName: IPointer[WORD], cchLocalName: int, ppwchType: IDoublePtr[WORD], pcchType: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PTR(PWORD), PINT)
    def getTypeFromQName(self, pwchQName: IPointer[WORD], cchQName: int, ppwchType: IDoublePtr[WORD], pcchType: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT, PTR(PWORD), PINT)
    def getValue(self, nIndex: int, ppwchValue: IDoublePtr[WORD], pcchValue: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PTR(PWORD), PINT)
    def getValueFromName(self, pwchUri: IPointer[WORD], cchUri: int, pwchLocalName: IPointer[WORD], cchLocalName: int, ppwchValue: IDoublePtr[WORD], pcchValue: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PWORD, INT, PTR(PWORD), PINT)
    def getValueFromQName(self, pwchQName: IPointer[WORD], cchQName: int, ppwchValue: IDoublePtr[WORD], pcchValue: IPointer[INT]) -> int: ...

    virtual_table.build()

class ISAXDTDHandler(IUnknown):
    """
    ISAXDTDHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{E15C1BAF-AFB3-4D60-8C36-19A8C45DEFED}")

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT)
    def notationDecl(self, pwchName: IPointer[WORD], cchName: int, pwchPublicId: IPointer[WORD], cchPublicId: int, pwchSystemId: IPointer[WORD], cchSystemId: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT, PWORD, INT)
    def unparsedEntityDecl(self, pwchName: IPointer[WORD], cchName: int, pwchPublicId: IPointer[WORD], cchPublicId: int, pwchSystemId: IPointer[WORD], cchSystemId: int, pwchNotationName: IPointer[WORD], cchNotationName: int) -> int: ...

    virtual_table.build()

class ISAXErrorHandler(IUnknown):
    """
    ISAXErrorHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{A60511C4-CCF5-479E-98A3-DC8DC545B7D0}")

    @virtual_table.com_function(PTR(ISAXLocator), PWORD, HRESULT)
    def error(self, pLocator: IPointer[ISAXLocator], pwchErrorMessage: IPointer[WORD], hrErrorCode: int) -> int: ...

    @virtual_table.com_function(PTR(ISAXLocator), PWORD, HRESULT)
    def fatalError(self, pLocator: IPointer[ISAXLocator], pwchErrorMessage: IPointer[WORD], hrErrorCode: int) -> int: ...

    @virtual_table.com_function(PTR(ISAXLocator), PWORD, HRESULT)
    def ignorableWarning(self, pLocator: IPointer[ISAXLocator], pwchErrorMessage: IPointer[WORD], hrErrorCode: int) -> int: ...

    virtual_table.build()

class ISAXXMLFilter(ISAXXMLReader):
    """
    ISAXXMLFilter interface
    """
    virtual_table = COMVirtualTable.from_ancestor(ISAXXMLReader)
    _iid_ = IID("{70409222-CA09-4475-ACB8-40312FE8D145}")

    @virtual_table.com_function(DOUBLE_PTR(ISAXXMLReader))
    def getParent(self, ppReader: IDoublePtr[ISAXXMLReader]) -> int: ...

    @virtual_table.com_function(PTR(ISAXXMLReader))
    def putParent(self, pReader: IPointer[ISAXXMLReader]) -> int: ...

    virtual_table.build()

class ISAXLexicalHandler(IUnknown):
    """
    ISAXLexicalHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7F85D5F5-47A8-4497-BDA5-84BA04819EA6}")

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT)
    def startDTD(self, pwchName: IPointer[WORD], cchName: int, pwchPublicId: IPointer[WORD], cchPublicId: int, pwchSystemId: IPointer[WORD], cchSystemId: int) -> int: ...

    @virtual_table.com_function()
    def endDTD(self) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def startEntity(self, pwchName: IPointer[WORD], cchName: int) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def endEntity(self, pwchName: IPointer[WORD], cchName: int) -> int: ...

    @virtual_table.com_function()
    def startCDATA(self) -> int: ...

    @virtual_table.com_function()
    def endCDATA(self) -> int: ...

    @virtual_table.com_function(PWORD, INT)
    def comment(self, pwchChars: IPointer[WORD], cchChars: int) -> int: ...

    virtual_table.build()

class ISAXDeclHandler(IUnknown):
    """
    ISAXDeclHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{862629AC-771A-47B2-8337-4E6843C1BE90}")

    @virtual_table.com_function(PWORD, INT, PWORD, INT)
    def elementDecl(self, pwchName: IPointer[WORD], cchName: int, pwchModel: IPointer[WORD], cchModel: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT, PWORD, INT, PWORD, INT)
    def attributeDecl(self, pwchElementName: IPointer[WORD], cchElementName: int, pwchAttributeName: IPointer[WORD], cchAttributeName: int, pwchType: IPointer[WORD], cchType: int, pwchValueDefault: IPointer[WORD], cchValueDefault: int, pwchValue: IPointer[WORD], cchValue: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT)
    def internalEntityDecl(self, pwchName: IPointer[WORD], cchName: int, pwchValue: IPointer[WORD], cchValue: int) -> int: ...

    @virtual_table.com_function(PWORD, INT, PWORD, INT, PWORD, INT)
    def externalEntityDecl(self, pwchName: IPointer[WORD], cchName: int, pwchPublicId: IPointer[WORD], cchPublicId: int, pwchSystemId: IPointer[WORD], cchSystemId: int) -> int: ...

    virtual_table.build()

class IVBSAXXMLReader(IDispatch):
    """
    IVBSAXXMLReader interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{8C033CAA-6CD6-4F73-B728-4531AF74945F}")

    @virtual_table.com_function(BSTR, PTR(BOOL))
    def getFeature(self, strName: BSTR, pOut: IPointer[BOOL]) -> int:
        """
        Look up the value of a feature.
        """
    @virtual_table.com_function(BSTR, BOOL)
    def putFeature(self, strName: BSTR, fValue: bool) -> int:
        """
        Set the state of a feature.
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getProperty(self, strName: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        Look up the value of a property.
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def putProperty(self, strName: BSTR, varValue: VARIANT) -> int:
        """
        Set the value of a property.
        """
    @virtual_table.com_function(PVOID)
    def get_entityResolver(self, ppOut: IDoublePtr['IVBSAXEntityResolver']) -> int:
        """
        Allow an application to register an entity resolver or look up the current entity resolver.
        """
    @virtual_table.com_function(PVOID)
    def entityResolver(self, param0: IPointer['IVBSAXEntityResolver']) -> int:
        """
        Allow an application to register an entity resolver or look up the current entity resolver.
        """
    @virtual_table.com_function(PVOID)
    def get_contentHandler(self, ppOut: IDoublePtr['IVBSAXContentHandler']) -> int:
        """
        Allow an application to register a content event handler or look up the current content event handler.
        """
    @virtual_table.com_function(PVOID)
    def contentHandler(self, param0: IPointer['IVBSAXContentHandler']) -> int:
        """
        Allow an application to register a content event handler or look up the current content event handler.
        """
    @virtual_table.com_function(PVOID)
    def get_dtdHandler(self, ppOut: IDoublePtr['IVBSAXDTDHandler']) -> int:
        """
        Allow an application to register a DTD event handler or look up the current DTD event handler.
        """
    @virtual_table.com_function(PVOID)
    def dtdHandler(self, param0: IPointer['IVBSAXDTDHandler']) -> int:
        """
        Allow an application to register a DTD event handler or look up the current DTD event handler.
        """
    @virtual_table.com_function(PVOID)
    def get_errorHandler(self, ppOut: IDoublePtr['IVBSAXErrorHandler']) -> int:
        """
        Allow an application to register an error event handler or look up the current error event handler.
        """
    @virtual_table.com_function(PVOID)
    def errorHandler(self, param0: IPointer['IVBSAXErrorHandler']) -> int:
        """
        Allow an application to register an error event handler or look up the current error event handler.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_baseURL(self, pOut: IPointer[BSTR]) -> int:
        """
        Set or get the base URL for the document.
        """
    @virtual_table.com_function(BSTR)
    def put_baseURL(self, param0: BSTR) -> int:
        """
        Set or get the base URL for the document.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_secureBaseURL(self, pOut: IPointer[BSTR]) -> int:
        """
        Set or get the secure base URL for the document.
        """
    @virtual_table.com_function(BSTR)
    def put_secureBaseURL(self, param0: BSTR) -> int:
        """
        Set or get the secure base URL for the document.
        """
    @virtual_table.com_function(VARIANT)
    def parse(self, varInput: VARIANT) -> int:
        """
        Parse an XML document.
        """
    @virtual_table.com_function(BSTR)
    def parseURL(self, strURL: BSTR) -> int:
        """
        Parse an XML document from a system identifier (URI).
        """
    virtual_table.build()

class IVBSAXEntityResolver(IDispatch):
    """
    IVBSAXEntityResolver interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{0C05D096-F45B-4ACA-AD1A-AA0BC25518DC}")

    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(VARIANT))
    def resolveEntity(self, strPublicId: IPointer[BSTR], strSystemId: IPointer[BSTR], pOut: IPointer[VARIANT]) -> int:
        """
        Allow the application to resolve external entities.
        """
    virtual_table.build()

class IVBSAXContentHandler(IDispatch):
    """
    IVBSAXContentHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2ED7290A-4DD5-4B46-BB26-4E4155E77FAA}")

    @virtual_table.com_function(PVOID)
    def documentLocator(self, param0: IPointer['IVBSAXLocator']) -> int:
        """
        Receive an object for locating the origin of SAX document events.
        """
    @virtual_table.com_function()
    def startDocument(self) -> int:
        """
        Receive notification of the beginning of a document.
        """
    @virtual_table.com_function()
    def endDocument(self) -> int:
        """
        Receive notification of the end of a document.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR))
    def startPrefixMapping(self, strPrefix: IPointer[BSTR], strURI: IPointer[BSTR]) -> int:
        """
        Begin the scope of a prefix-URI Namespace mapping.
        """
    @virtual_table.com_function(PTR(BSTR))
    def endPrefixMapping(self, strPrefix: IPointer[BSTR]) -> int:
        """
        End the scope of a prefix-URI mapping.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR), PVOID)
    def startElement(self, strNamespaceURI: IPointer[BSTR], strLocalName: IPointer[BSTR], strQName: IPointer[BSTR], oAttributes: IPointer['IVBSAXAttributes']) -> int:
        """
        Receive notification of the beginning of an element.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def endElement(self, strNamespaceURI: IPointer[BSTR], strLocalName: IPointer[BSTR], strQName: IPointer[BSTR]) -> int:
        """
        Receive notification of the end of an element.
        """
    @virtual_table.com_function(PTR(BSTR))
    def characters(self, strChars: IPointer[BSTR]) -> int:
        """
        Receive notification of character data.
        """
    @virtual_table.com_function(PTR(BSTR))
    def ignorableWhitespace(self, strChars: IPointer[BSTR]) -> int:
        """
        Receive notification of ignorable whitespace in element content.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR))
    def processingInstruction(self, strTarget: IPointer[BSTR], strData: IPointer[BSTR]) -> int:
        """
        Receive notification of a processing instruction.
        """
    @virtual_table.com_function(PTR(BSTR))
    def skippedEntity(self, strName: IPointer[BSTR]) -> int:
        """
        Receive notification of a skipped entity.
        """
    virtual_table.build()

class IVBSAXLocator(IDispatch):
    """
    IVBSAXLocator interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{796E7AC5-5AA2-4EFF-ACAD-3FAAF01A3288}")

    @virtual_table.com_function(PINT)
    def get_columnNumber(self, pOut: IPointer[INT]) -> int:
        """
        Get the column number where the current document event ends.
        """
    @virtual_table.com_function(PINT)
    def get_lineNumber(self, pOut: IPointer[INT]) -> int:
        """
        Get the line number where the current document event ends.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_publicId(self, pOut: IPointer[BSTR]) -> int:
        """
        Get the public identifier for the current document event.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_systemId(self, pOut: IPointer[BSTR]) -> int:
        """
        Get the system identifier for the current document event.
        """
    virtual_table.build()

class IVBSAXAttributes(IDispatch):
    """
    IVBSAXAttributes interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{10DC0586-132B-4CAC-8BB3-DB00AC8B7EE0}")

    @virtual_table.com_function(PINT)
    def get_length(self, pOut: IPointer[INT]) -> int:
        """
        Get the number of attributes in the list.
        """
    @virtual_table.com_function(INT, PTR(BSTR))
    def getURI(self, nIndex: int, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's Namespace URI by index.
        """
    @virtual_table.com_function(INT, PTR(BSTR))
    def getLocalName(self, nIndex: int, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's local name by index.
        """
    @virtual_table.com_function(INT, PTR(BSTR))
    def getQName(self, nIndex: int, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's XML 1.0 qualified name by index.
        """
    @virtual_table.com_function(BSTR, BSTR, PINT)
    def getIndexFromName(self, strURI: BSTR, strLocalName: BSTR, pOut: IPointer[INT]) -> int:
        """
        Look up the index of an attribute by Namespace name.
        """
    @virtual_table.com_function(BSTR, PINT)
    def getIndexFromQName(self, strQName: BSTR, pOut: IPointer[INT]) -> int:
        """
        Look up the index of an attribute by XML 1.0 qualified name.
        """
    @virtual_table.com_function(INT, PTR(BSTR))
    def getType(self, nIndex: int, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's type by index.
        """
    @virtual_table.com_function(BSTR, BSTR, PTR(BSTR))
    def getTypeFromName(self, strURI: BSTR, strLocalName: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's type by Namespace name.
        """
    @virtual_table.com_function(BSTR, PTR(BSTR))
    def getTypeFromQName(self, strQName: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's type by XML 1.0 qualified name.
        """
    @virtual_table.com_function(INT, PTR(BSTR))
    def getValue(self, nIndex: int, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's value by index.
        """
    @virtual_table.com_function(BSTR, BSTR, PTR(BSTR))
    def getValueFromName(self, strURI: BSTR, strLocalName: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's value by Namespace name.
        """
    @virtual_table.com_function(BSTR, PTR(BSTR))
    def getValueFromQName(self, strQName: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Look up an attribute's value by XML 1.0 qualified name.
        """
    virtual_table.build()

class IVBSAXDTDHandler(IDispatch):
    """
    IVBSAXDTDHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{24FB3297-302D-4620-BA39-3A732D850558}")

    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def notationDecl(self, strName: IPointer[BSTR], strPublicId: IPointer[BSTR], strSystemId: IPointer[BSTR]) -> int:
        """
        Receive notification of a notation declaration event.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def unparsedEntityDecl(self, strName: IPointer[BSTR], strPublicId: IPointer[BSTR], strSystemId: IPointer[BSTR], strNotationName: IPointer[BSTR]) -> int:
        """
        Receive notification of an unparsed entity declaration event.
        """
    virtual_table.build()

class IVBSAXErrorHandler(IDispatch):
    """
    IVBSAXErrorHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{D963D3FE-173C-4862-9095-B92F66995F52}")

    @virtual_table.com_function(PTR(IVBSAXLocator), PTR(BSTR), LONG)
    def error(self, oLocator: IPointer[IVBSAXLocator], strErrorMessage: IPointer[BSTR], nErrorCode: int) -> int:
        """
        Receive notification of a recoverable error.
        """
    @virtual_table.com_function(PTR(IVBSAXLocator), PTR(BSTR), LONG)
    def fatalError(self, oLocator: IPointer[IVBSAXLocator], strErrorMessage: IPointer[BSTR], nErrorCode: int) -> int:
        """
        Receive notification of a non-recoverable error.
        """
    @virtual_table.com_function(PTR(IVBSAXLocator), PTR(BSTR), LONG)
    def ignorableWarning(self, oLocator: IPointer[IVBSAXLocator], strErrorMessage: IPointer[BSTR], nErrorCode: int) -> int:
        """
        Receive notification of an ignorable warning.
        """
    virtual_table.build()

class IVBSAXXMLFilter(IDispatch):
    """
    IVBSAXXMLFilter interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{1299EB1B-5B88-433E-82DE-82CA75AD4E04}")

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXXMLReader))
    def get_parent(self, ppOut: IDoublePtr[IVBSAXXMLReader]) -> int:
        """
        Set or get the parent reader
        """
    @virtual_table.com_function(PTR(IVBSAXXMLReader))
    def parent(self, param0: IPointer[IVBSAXXMLReader]) -> int:
        """
        Set or get the parent reader
        """
    virtual_table.build()

class IVBSAXLexicalHandler(IDispatch):
    """
    IVBSAXLexicalHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{032AAC35-8C0E-4D9D-979F-E3B702935576}")

    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def startDTD(self, strName: IPointer[BSTR], strPublicId: IPointer[BSTR], strSystemId: IPointer[BSTR]) -> int:
        """
        Report the start of DTD declarations, if any.
        """
    @virtual_table.com_function()
    def endDTD(self) -> int:
        """
        Report the end of DTD declarations.
        """
    @virtual_table.com_function(PTR(BSTR))
    def startEntity(self, strName: IPointer[BSTR]) -> int:
        """
        Report the beginning of some internal and external XML entities.
        """
    @virtual_table.com_function(PTR(BSTR))
    def endEntity(self, strName: IPointer[BSTR]) -> int:
        """
        Report the end of an entity.
        """
    @virtual_table.com_function()
    def startCDATA(self) -> int:
        """
        Report the start of a CDATA section.
        """
    @virtual_table.com_function()
    def endCDATA(self) -> int:
        """
        Report the end of a CDATA section.
        """
    @virtual_table.com_function(PTR(BSTR))
    def comment(self, strChars: IPointer[BSTR]) -> int:
        """
        Report an XML comment anywhere in the document.
        """
    virtual_table.build()

class IVBSAXDeclHandler(IDispatch):
    """
    IVBSAXDeclHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{E8917260-7579-4BE1-B5DD-7AFBFA6F077B}")

    @virtual_table.com_function(PTR(BSTR), PTR(BSTR))
    def elementDecl(self, strName: IPointer[BSTR], strModel: IPointer[BSTR]) -> int:
        """
        Report an element type declaration.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def attributeDecl(self, strElementName: IPointer[BSTR], strAttributeName: IPointer[BSTR], strType: IPointer[BSTR], strValueDefault: IPointer[BSTR], strValue: IPointer[BSTR]) -> int:
        """
        Report an attribute type declaration.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR))
    def internalEntityDecl(self, strName: IPointer[BSTR], strValue: IPointer[BSTR]) -> int:
        """
        Report an internal entity declaration.
        """
    @virtual_table.com_function(PTR(BSTR), PTR(BSTR), PTR(BSTR))
    def externalEntityDecl(self, strName: IPointer[BSTR], strPublicId: IPointer[BSTR], strSystemId: IPointer[BSTR]) -> int:
        """
        Report a parsed external entity declaration.
        """
    virtual_table.build()

class IMXWriter(IDispatch):
    """
    IMXWriter interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{4D7FF4BA-1565-4EA8-94E1-6E724A46F98D}")

    @virtual_table.com_function(VARIANT)
    def put_output(self, param0: VARIANT) -> int:
        """
        Set or get the output.
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_output(self, pOut: IPointer[VARIANT]) -> int:
        """
        Set or get the output.
        """
    @virtual_table.com_function(BSTR)
    def put_encoding(self, param0: BSTR) -> int:
        """
        Set or get the output encoding.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_encoding(self, pOut: IPointer[BSTR]) -> int:
        """
        Set or get the output encoding.
        """
    @virtual_table.com_function(BOOL)
    def put_byteOrderMark(self, param0: bool) -> int:
        """
        Determine whether or not to write the byte order mark
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_byteOrderMark(self, pOut: IPointer[BOOL]) -> int:
        """
        Determine whether or not to write the byte order mark
        """
    @virtual_table.com_function(BOOL)
    def put_indent(self, param0: bool) -> int:
        """
        Enable or disable auto indent mode.
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_indent(self, pOut: IPointer[BOOL]) -> int:
        """
        Enable or disable auto indent mode.
        """
    @virtual_table.com_function(BOOL)
    def put_standalone(self, param0: bool) -> int:
        """
        Set or get the standalone document declaration.
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_standalone(self, pOut: IPointer[BOOL]) -> int:
        """
        Set or get the standalone document declaration.
        """
    @virtual_table.com_function(BOOL)
    def put_omitXMLDeclaration(self, param0: bool) -> int:
        """
        Determine whether or not to omit the XML declaration.
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_omitXMLDeclaration(self, pOut: IPointer[BOOL]) -> int:
        """
        Determine whether or not to omit the XML declaration.
        """
    @virtual_table.com_function(BSTR)
    def put_version(self, param0: BSTR) -> int:
        """
        Set or get the xml version info.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_version(self, pOut: IPointer[BSTR]) -> int:
        """
        Set or get the xml version info.
        """
    @virtual_table.com_function(BOOL)
    def put_disableOutputEscaping(self, param0: bool) -> int:
        """
        When enabled, the writer no longer escapes out its input when writing it out.
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_disableOutputEscaping(self, pOut: IPointer[BOOL]) -> int:
        """
        When enabled, the writer no longer escapes out its input when writing it out.
        """
    @virtual_table.com_function()
    def flush(self) -> int:
        """
        Flushes all writer buffers forcing the writer to write to the underlying output object
        """
    virtual_table.build()

class IMXAttributes(IDispatch):
    """
    IMXAttributes interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{F10D27CC-3EC0-415C-8ED8-77AB1C5E7262}")

    @virtual_table.com_function(BSTR, BSTR, BSTR, BSTR, BSTR)
    def addAttribute(self, strURI: BSTR, strLocalName: BSTR, strQName: BSTR, strType: BSTR, strValue: BSTR) -> int:
        """
        Add an attribute to the end of the list.
        """
    @virtual_table.com_function(VARIANT, INT)
    def addAttributeFromIndex(self, varAtts: VARIANT, nIndex: int) -> int:
        """
        Add an attribute, whose value is equal to the indexed attribute in the input attributes object, to the end of the list.
        """
    @virtual_table.com_function()
    def clear(self) -> int:
        """
        Clear the attribute list for reuse.
        """
    @virtual_table.com_function(INT)
    def removeAttribute(self, nIndex: int) -> int:
        """
        Remove an attribute from the list.
        """
    @virtual_table.com_function(INT, BSTR, BSTR, BSTR, BSTR, BSTR)
    def setAttribute(self, nIndex: int, strURI: BSTR, strLocalName: BSTR, strQName: BSTR, strType: BSTR, strValue: BSTR) -> int:
        """
        Set an attribute in the list.
        """
    @virtual_table.com_function(VARIANT)
    def setAttributes(self, varAtts: VARIANT) -> int:
        """
        Copy an entire Attributes object.
        """
    @virtual_table.com_function(INT, BSTR)
    def setLocalName(self, nIndex: int, strLocalName: BSTR) -> int:
        """
        Set the local name of a specific attribute.
        """
    @virtual_table.com_function(INT, BSTR)
    def setQName(self, nIndex: int, strQName: BSTR) -> int:
        """
        Set the qualified name of a specific attribute.
        """
    @virtual_table.com_function(INT, BSTR)
    def setType(self, nIndex: int, strType: BSTR) -> int:
        """
        Set the type of a specific attribute.
        """
    @virtual_table.com_function(INT, BSTR)
    def setURI(self, nIndex: int, strURI: BSTR) -> int:
        """
        Set the Namespace URI of a specific attribute.
        """
    @virtual_table.com_function(INT, BSTR)
    def setValue(self, nIndex: int, strValue: BSTR) -> int:
        """
        Set the value of a specific attribute.
        """
    virtual_table.build()

class IMXReaderControl(IDispatch):
    """
    IMXReaderControl interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{808F4E35-8D5A-4FBE-8466-33A41279ED30}")

    @virtual_table.com_function()
    def abort(self) -> int:
        """
        Abort the reader
        """
    @virtual_table.com_function()
    def resume(self) -> int:
        """
        Resume the reader
        """
    @virtual_table.com_function()
    def suspend(self) -> int:
        """
        Suspend the reader
        """
    virtual_table.build()

class IMXSchemaDeclHandler(IDispatch):
    """
    IMXSchemaDeclHandler interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{FA4BB38C-FAF9-4CCA-9302-D1DD0FE520DB}")

    @virtual_table.com_function(PVOID)
    def schemaElementDecl(self, oSchemaElement: IPointer['ISchemaElement']) -> int:
        """
        Access schema element declaration
        """
    virtual_table.build()

class ISchemaElement(IDispatch):
    """
    XML Schema Element
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B7-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_schema(self, ppOut: IDoublePtr['ISchema']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_type(self, ppOut: IDoublePtr['ISchemaType']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_scope(self, ppOut: IDoublePtr['ISchemaComplexType']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_defaultValue(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fixedValue(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_isNillable(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_identityConstraints(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_substitutionGroup(self, ppOut: IDoublePtr['ISchemaElement']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_substitutionGroupExclusions(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_disallowedSubstitutions(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_isAbstract(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_isReference(self, pOut: IPointer[BOOL]) -> int: ...

    virtual_table.build()

class ISchemaParticle(IDispatch):
    """
    XML Schema Particle
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B5-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_schema(self, ppOut: IDoublePtr['ISchema']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    virtual_table.build()

class ISchemaItem(IDispatch):
    """
    XML Schema Item
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B3-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_schema(self, ppOut: IDoublePtr['ISchema']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    virtual_table.build()

class ISchema(IDispatch):
    """
    XML Schema
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B4-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_schema(self, ppOut: IDoublePtr['ISchema']) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_targetNamespace(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_version(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_types(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_elements(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_attributes(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_attributeGroups(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_modelGroups(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_notations(self, ppOut: IDoublePtr['ISchemaItemCollection']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_schemaLocations(self, ppOut: IDoublePtr['ISchemaStringCollection']) -> int: ...

    virtual_table.build()

class ISchemaItemCollection(IDispatch):
    """
    XML Schema Item Collection
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B2-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(LONG, DOUBLE_PTR(ISchemaItem))
    def get_item(self, index: int, ppOut: IDoublePtr[ISchemaItem]) -> int: ...

    @virtual_table.com_function(BSTR, DOUBLE_PTR(ISchemaItem))
    def itemByName(self, name: BSTR, ppOut: IDoublePtr[ISchemaItem]) -> int: ...

    @virtual_table.com_function(BSTR, BSTR, DOUBLE_PTR(ISchemaItem))
    def itemByQName(self, name: BSTR, namespaceURI: BSTR, ppOut: IDoublePtr[ISchemaItem]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class ISchemaStringCollection(IDispatch):
    """
    XML Schema String Collection
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B1-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(LONG, PTR(BSTR))
    def get_item(self, index: int, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class ISchemaType(IDispatch):
    """
    XML Schema Type
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B8-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaItemCollection))
    def get_baseTypes(self, ppOut: IDoublePtr[ISchemaItemCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_final(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_variety(self, pOut: IPointer['SCHEMATYPEVARIETY']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_derivedBy(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(BSTR, PTR(BOOL))
    def isValid(self, data: BSTR, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_minExclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_minInclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_maxExclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_maxInclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_totalDigits(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_fractionDigits(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_length(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minLength(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxLength(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_enumeration(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_whitespace(self, pOut: IPointer['SCHEMAWHITESPACE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_patterns(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    virtual_table.build()

class ISchemaComplexType(IDispatch):
    """
    XML Schema Complex Type
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B9-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaItemCollection))
    def get_baseTypes(self, ppOut: IDoublePtr[ISchemaItemCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_final(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_variety(self, pOut: IPointer['SCHEMATYPEVARIETY']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_derivedBy(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    @virtual_table.com_function(BSTR, PTR(BOOL))
    def isValid(self, data: BSTR, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_minExclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_minInclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_maxExclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_maxInclusive(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_totalDigits(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_fractionDigits(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_length(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minLength(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxLength(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_enumeration(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_whitespace(self, pOut: IPointer['SCHEMAWHITESPACE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_patterns(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_isAbstract(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_anyAttribute(self, ppOut: IDoublePtr['ISchemaAny']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaItemCollection))
    def get_attributes(self, ppOut: IDoublePtr[ISchemaItemCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_contentType(self, pOut: IPointer['SCHEMACONTENTTYPE']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_contentModel(self, ppOut: IDoublePtr['ISchemaModelGroup']) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_prohibitedSubstitutions(self, pOut: IPointer['SCHEMADERIVATIONMETHOD']) -> int: ...

    virtual_table.build()

class ISchemaAny(IDispatch):
    """
    XML Schema Any
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08BC-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_namespaces(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_processContents(self, pOut: IPointer['SCHEMAPROCESSCONTENTS']) -> int: ...

    virtual_table.build()

class ISchemaModelGroup(IDispatch):
    """
    XML Schema Type
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08BB-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_minOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PTR(VARIANT))
    def get_maxOccurs(self, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaItemCollection))
    def get_particles(self, ppOut: IDoublePtr[ISchemaItemCollection]) -> int: ...

    virtual_table.build()

class IMXXMLFilter(IDispatch):
    """
    IMXXMLFilter interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{C90352F7-643C-4FBC-BB23-E996EB2D51FD}")

    @virtual_table.com_function(BSTR, PTR(BOOL))
    def getFeature(self, strName: BSTR, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(BSTR, BOOL)
    def putFeature(self, strName: BSTR, fValue: bool) -> int: ...

    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getProperty(self, strName: BSTR, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(BSTR, VARIANT)
    def putProperty(self, strName: BSTR, varValue: VARIANT) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get_entityResolver(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def entityResolver(self, param0: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get_contentHandler(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def contentHandler(self, param0: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get_dtdHandler(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def dtdHandler(self, param0: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get_errorHandler(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def errorHandler(self, param0: IPointer[IUnknown]) -> int: ...

    virtual_table.build()

class IXMLDOMSchemaCollection2(IDispatch):
    """
    XML Schemas Collection 2
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B0-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(BSTR, VARIANT)
    def add(self, namespaceURI: BSTR, var: VARIANT) -> int:
        """
        add a new schema
        """
    @virtual_table.com_function(BSTR, DOUBLE_PTR(IXMLDOMNode))
    def get(self, namespaceURI: BSTR, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        lookup schema by namespaceURI
        """
    @virtual_table.com_function(BSTR)
    def remove(self, namespaceURI: BSTR) -> int:
        """
        remove schema by namespaceURI
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of schemas in collection
        """
    @virtual_table.com_function(LONG, PTR(BSTR))
    def get_namespaceURI(self, index: int, pOut: IPointer[BSTR]) -> int:
        """
        Get namespaceURI for schema by index
        """
    @virtual_table.com_function(PTR(IXMLDOMSchemaCollection))
    def addCollection(self, otherCollection: IPointer[IXMLDOMSchemaCollection]) -> int:
        """
        copy & merge other collection into this one
        """
    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function()
    def validate(self) -> int: ...

    @virtual_table.com_function(BOOL)
    def put_validateOnLoad(self, param0: bool) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_validateOnLoad(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(BSTR, DOUBLE_PTR(ISchema))
    def getSchema(self, namespaceURI: BSTR, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(ISchemaItem))
    def getDeclaration(self, node: IPointer[IXMLDOMNode], ppOut: IDoublePtr[ISchemaItem]) -> int: ...

    virtual_table.build()

class ISchemaAttribute(IDispatch):
    """
    XML Schema Attribute
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08B6-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaType))
    def get_type(self, ppOut: IDoublePtr[ISchemaType]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaComplexType))
    def get_scope(self, ppOut: IDoublePtr[ISchemaComplexType]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_defaultValue(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fixedValue(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_use(self, pOut: IPointer['SCHEMAUSE']) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_isReference(self, pOut: IPointer[BOOL]) -> int: ...

    virtual_table.build()

class ISchemaAttributeGroup(IDispatch):
    """
    XML Schema Attribute Group
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08BA-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaAny))
    def get_anyAttribute(self, ppOut: IDoublePtr[ISchemaAny]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaItemCollection))
    def get_attributes(self, ppOut: IDoublePtr[ISchemaItemCollection]) -> int: ...

    virtual_table.build()

class ISchemaIdentityConstraint(IDispatch):
    """
    XML Schema Any
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08BD-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_selector(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchemaStringCollection))
    def get_fields(self, ppOut: IDoublePtr[ISchemaStringCollection]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_referencedKey(self, ppOut: IDoublePtr['ISchemaIdentityConstraint']) -> int: ...

    virtual_table.build()

class ISchemaNotation(IDispatch):
    """
    XML Schema Notation
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{50EA08BE-DD1B-4664-9A50-C2F40F4BD79A}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_namespaceURI(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ISchema))
    def get_schema(self, ppOut: IDoublePtr[ISchema]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_id(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PVOID)
    def get_itemType(self, pOut: IPointer['SOMITEMTYPE']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IVBSAXAttributes))
    def get_unhandledAttributes(self, ppOut: IDoublePtr[IVBSAXAttributes]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN, PTR(BOOL))
    def writeAnnotation(self, annotationSink: IPointer[IUnknown], pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_systemIdentifier(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_publicIdentifier(self, pOut: IPointer[BSTR]) -> int: ...

    virtual_table.build()

class IXMLElementCollection(IDispatch):
    """
    IXMLElementCollection helps to enumerate through a XML document tree.
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{65725580-9B5D-11D0-9BFE-00C04FC99C8E}")

    @virtual_table.com_function(LONG)
    def put_length(self, param0: int) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(VARIANT, VARIANT, DOUBLE_PTR(IDispatch))
    def item(self, var1: VARIANT, var2: VARIANT, ppOut: IDoublePtr[IDispatch]) -> int:
        """
        get current item, or (optional) by index and name.
        """
    virtual_table.build()

class IXMLDocument(IDispatch):
    """
    IXMLDocument loads and saves XML document. This is obsolete. You should use IDOMDocument or IXMLDOMDocument.
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{F52E2B61-18A1-11D1-B105-00805F49916B}")

    @virtual_table.com_function(PVOID)
    def get_root(self, ppOut: IDoublePtr['IXMLElement']) -> int:
        """
        get root IXMLElement of the XML document.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_fileSize(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fileModifiedDate(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fileUpdatedDate(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, pOut: IPointer[BSTR]) -> int:
        """
        set URL to load an XML document from the URL.
        """
    @virtual_table.com_function(BSTR)
    def put_url(self, param0: BSTR) -> int:
        """
        set URL to load an XML document from the URL.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_mimeType(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        get ready state.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_charset(self, pOut: IPointer[BSTR]) -> int:
        """
        get encoding.
        """
    @virtual_table.com_function(BSTR)
    def put_charset(self, param0: BSTR) -> int:
        """
        get encoding.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_version(self, pOut: IPointer[BSTR]) -> int:
        """
        get XML version number.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_doctype(self, pOut: IPointer[BSTR]) -> int:
        """
        get document type.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_dtdURL(self, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(VARIANT, VARIANT, PVOID)
    def createElement(self, vType: VARIANT, var1: VARIANT, ppOut: IDoublePtr['IXMLElement']) -> int:
        """
        create different types of IXMLElements.
        """
    virtual_table.build()

class IXMLElement(IDispatch):
    """
    IXMLElement represents an element in the XML document tree.
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{3F7F31AC-E15F-11D0-9C25-00C04FC99C8E}")

    @virtual_table.com_function(PTR(BSTR))
    def get_tagName(self, pOut: IPointer[BSTR]) -> int:
        """
        get tag name.
        """
    @virtual_table.com_function(BSTR)
    def put_tagName(self, param0: BSTR) -> int:
        """
        get tag name.
        """
    @virtual_table.com_function(PVOID)
    def get_parent(self, ppOut: IDoublePtr['IXMLElement']) -> int:
        """
        get parent IXMLElement.
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setAttribute(self, strPropertyName: BSTR, PropertyValue: VARIANT) -> int:
        """
        set attribute.
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getAttribute(self, strPropertyName: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        get attribute.
        """
    @virtual_table.com_function(BSTR)
    def removeAttribute(self, strPropertyName: BSTR) -> int:
        """
        remove attribute.
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLElementCollection))
    def get_children(self, ppOut: IDoublePtr[IXMLElementCollection]) -> int:
        """
        get a IXMLElementCollection of children.
        """
    @virtual_table.com_function(PLONG)
    def get_type(self, pOut: IPointer[LONG]) -> int:
        """
        get type of this IXMLElement.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        get text.
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        get text.
        """
    @virtual_table.com_function(PVOID, LONG, LONG)
    def addChild(self, pChildElem: IPointer['IXMLElement'], lIndex: int, lReserved: int) -> int:
        """
        add a child.
        """
    @virtual_table.com_function(PVOID)
    def removeChild(self, pChildElem: IPointer['IXMLElement']) -> int:
        """
        remove a child.
        """
    virtual_table.build()

class IXMLDocument2(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2B8DE2FE-8D2D-11D1-B2FC-00C04FD915A9}")

    @virtual_table.com_function(PVOID)
    def get_root(self, p: IDoublePtr['IXMLElement2']) -> int:
        """
        get root IXMLElement of the XML document.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_fileSize(self, p: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fileModifiedDate(self, p: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_fileUpdatedDate(self, p: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_url(self, p: IPointer[BSTR]) -> int:
        """
        set URL to load an XML document from the URL.
        """
    @virtual_table.com_function(BSTR)
    def put_url(self, p: BSTR) -> int:
        """
        set URL to load an XML document from the URL.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_mimeType(self, p: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_readyState(self, pl: IPointer[LONG]) -> int:
        """
        get ready state.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_charset(self, p: IPointer[BSTR]) -> int:
        """
        get encoding.
        """
    @virtual_table.com_function(BSTR)
    def put_charset(self, p: BSTR) -> int:
        """
        get encoding.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_version(self, p: IPointer[BSTR]) -> int:
        """
        get XML version number.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_doctype(self, p: IPointer[BSTR]) -> int:
        """
        get document type.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_dtdURL(self, p: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(VARIANT, VARIANT, PVOID)
    def createElement(self, vType: VARIANT, var1: VARIANT, ppElem: IDoublePtr['IXMLElement2']) -> int:
        """
        create different types of IXMLElements.
        """
    @virtual_table.com_function(PTR(BOOL))
    def get_async(self, pf: IPointer[BOOL]) -> int:
        """
        get asynchronous loading flag.
        """
    @virtual_table.com_function(BOOL)
    def put_async(self, pf: bool) -> int:
        """
        get asynchronous loading flag.
        """
    virtual_table.build()

class IXMLElement2(IDispatch):
    """
    IXMLElement2 extends IXMLElement.
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2B8DE2FF-8D2D-11D1-B2FC-00C04FD915A9}")

    @virtual_table.com_function(PTR(BSTR))
    def get_tagName(self, pOut: IPointer[BSTR]) -> int:
        """
        get tag name.
        """
    @virtual_table.com_function(BSTR)
    def put_tagName(self, param0: BSTR) -> int:
        """
        get tag name.
        """
    @virtual_table.com_function(PVOID)
    def get_parent(self, ppOut: IDoublePtr['IXMLElement2']) -> int:
        """
        get parent IXMLElement.
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setAttribute(self, strPropertyName: BSTR, PropertyValue: VARIANT) -> int:
        """
        set attribute.
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getAttribute(self, strPropertyName: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        get attribute.
        """
    @virtual_table.com_function(BSTR)
    def removeAttribute(self, strPropertyName: BSTR) -> int:
        """
        remove attribute.
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLElementCollection))
    def get_children(self, ppOut: IDoublePtr[IXMLElementCollection]) -> int:
        """
        get a IXMLElementCollection of all children.
        """
    @virtual_table.com_function(PLONG)
    def get_type(self, pOut: IPointer[LONG]) -> int:
        """
        get type of this IXMLElement.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_text(self, pOut: IPointer[BSTR]) -> int:
        """
        get text.
        """
    @virtual_table.com_function(BSTR)
    def put_text(self, param0: BSTR) -> int:
        """
        get text.
        """
    @virtual_table.com_function(PVOID, LONG, LONG)
    def addChild(self, pChildElem: IPointer['IXMLElement2'], lIndex: int, lReserved: int) -> int:
        """
        add a child.
        """
    @virtual_table.com_function(PVOID)
    def removeChild(self, pChildElem: IPointer['IXMLElement2']) -> int:
        """
        remove a child.
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLElementCollection))
    def get_attributes(self, ppOut: IDoublePtr[IXMLElementCollection]) -> int:
        """
        get a IXMLElementCollection of all attributes.
        """
    virtual_table.build()

class IXMLAttribute(IDispatch):
    """
    IXMLAttribute allows to get attributes of an IXMLElement.
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{D4D4A0FC-3B73-11D1-B2B4-00C04FB92596}")

    @virtual_table.com_function(PTR(BSTR))
    def get_name(self, pOut: IPointer[BSTR]) -> int:
        """
        get attribute name.
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_value(self, pOut: IPointer[BSTR]) -> int:
        """
        get attribute value.
        """
    virtual_table.build()

class IXMLError(IUnknown):
    """
    Gets error info.
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{948C5AD3-C58D-11D0-9C0B-00C04FC99C8E}")

    @virtual_table.com_function(PTR(_xml_error))
    def GetErrorInfo(self, pErrorReturn: IPointer[_xml_error]) -> int: ...

    virtual_table.build()

class IXMLDOMSelection(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{AA634FC7-5888-44A7-A257-3A47150D3A0E}")

    @virtual_table.com_function(LONG, DOUBLE_PTR(IXMLDOMNode))
    def get_item(self, index: int, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        collection of nodes
        """
    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int:
        """
        number of nodes in the collection
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def nextNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        get next node from iterator
        """
    @virtual_table.com_function()
    def reset(self) -> int:
        """
        reset the position of iterator
        """
    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(BSTR))
    def get_expr(self, pOut: IPointer[BSTR]) -> int:
        """
        selection expression
        """
    @virtual_table.com_function(BSTR)
    def put_expr(self, param0: BSTR) -> int:
        """
        selection expression
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def get_context(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        nodes to apply selection expression to
        """
    @virtual_table.com_function(PTR(IXMLDOMNode))
    def context(self, param0: IPointer[IXMLDOMNode]) -> int:
        """
        nodes to apply selection expression to
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def peekNode(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        gets the next node without advancing the list position
        """
    @virtual_table.com_function(PTR(IXMLDOMNode), DOUBLE_PTR(IXMLDOMNode))
    def matches(self, pNode: IPointer[IXMLDOMNode], ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        checks to see if the node matches the pattern
        """
    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMNode))
    def removeNext(self, ppOut: IDoublePtr[IXMLDOMNode]) -> int:
        """
        removes the next node
        """
    @virtual_table.com_function()
    def removeAll(self) -> int:
        """
        removes all the nodes that match the selection
        """
    @virtual_table.com_function(PVOID)
    def clone(self, ppOut: IDoublePtr['IXMLDOMSelection']) -> int:
        """
        clone this object with the same position and context
        """
    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getProperty(self, name: BSTR, pOut: IPointer[VARIANT]) -> int:
        """
        get the value of the named property
        """
    @virtual_table.com_function(BSTR, VARIANT)
    def setProperty(self, name: BSTR, value: VARIANT) -> int:
        """
        set the value of the named property
        """
    virtual_table.build()

class IDSOControl(IDispatch):
    """
    DSO Control
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{310AFA62-0575-11D2-9CA9-0060B0EC3D39}")

    @virtual_table.com_function(DOUBLE_PTR(IXMLDOMDocument))
    def get_XMLDocument(self, ppOut: IDoublePtr[IXMLDOMDocument]) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMDocument))
    def put_XMLDocument(self, param0: IPointer[IXMLDOMDocument]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_JavaDSOCompatible(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(LONG)
    def put_JavaDSOCompatible(self, param0: int) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int: ...

    virtual_table.build()

class IXMLHTTPRequest(IDispatch):
    """
    IXMLHTTPRequest Interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{ED8C108D-4349-11D2-91A4-00C04F7969E8}")

    @virtual_table.com_function(BSTR, BSTR, VARIANT, VARIANT, VARIANT)
    def open(self, bstrMethod: BSTR, bstrUrl: BSTR, varAsync: VARIANT, bstrUser: VARIANT, bstrPassword: VARIANT) -> int:
        """
        Open HTTP connection
        """
    @virtual_table.com_function(BSTR, BSTR)
    def setRequestHeader(self, bstrHeader: BSTR, bstrValue: BSTR) -> int:
        """
        Add HTTP request header
        """
    @virtual_table.com_function(BSTR, PTR(BSTR))
    def getResponseHeader(self, bstrHeader: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP response header
        """
    @virtual_table.com_function(PTR(BSTR))
    def getAllResponseHeaders(self, pOut: IPointer[BSTR]) -> int:
        """
        Get all HTTP response headers
        """
    @virtual_table.com_function(VARIANT)
    def send(self, varBody: VARIANT) -> int:
        """
        Send HTTP request
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        Abort HTTP request
        """
    @virtual_table.com_function(PLONG)
    def get_status(self, pOut: IPointer[LONG]) -> int:
        """
        Get HTTP status code
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_statusText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP status text
        """
    @virtual_table.com_function(DOUBLE_PTR(IDispatch))
    def get_responseXML(self, ppOut: IDoublePtr[IDispatch]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_responseText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseBody(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseStream(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        Get ready state
        """
    @virtual_table.com_function(PTR(IDispatch))
    def put_onreadystatechange(self, param0: IPointer[IDispatch]) -> int:
        """
        Register a complete event handler
        """
    virtual_table.build()

class IServerXMLHTTPRequest(IDispatch):
    """
    IServerXMLHTTPRequest Interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2E9196BF-13BA-4DD4-91CA-6C571F281495}")

    @virtual_table.com_function(BSTR, BSTR, VARIANT, VARIANT, VARIANT)
    def open(self, bstrMethod: BSTR, bstrUrl: BSTR, varAsync: VARIANT, bstrUser: VARIANT, bstrPassword: VARIANT) -> int:
        """
        Open HTTP connection
        """
    @virtual_table.com_function(BSTR, BSTR)
    def setRequestHeader(self, bstrHeader: BSTR, bstrValue: BSTR) -> int:
        """
        Add HTTP request header
        """
    @virtual_table.com_function(BSTR, PTR(BSTR))
    def getResponseHeader(self, bstrHeader: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP response header
        """
    @virtual_table.com_function(PTR(BSTR))
    def getAllResponseHeaders(self, pOut: IPointer[BSTR]) -> int:
        """
        Get all HTTP response headers
        """
    @virtual_table.com_function(VARIANT)
    def send(self, varBody: VARIANT) -> int:
        """
        Send HTTP request
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        Abort HTTP request
        """
    @virtual_table.com_function(PLONG)
    def get_status(self, pOut: IPointer[LONG]) -> int:
        """
        Get HTTP status code
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_statusText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP status text
        """
    @virtual_table.com_function(DOUBLE_PTR(IDispatch))
    def get_responseXML(self, ppOut: IDoublePtr[IDispatch]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_responseText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseBody(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseStream(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        Get ready state
        """
    @virtual_table.com_function(PTR(IDispatch))
    def put_onreadystatechange(self, param0: IPointer[IDispatch]) -> int:
        """
        Register a complete event handler
        """
    @virtual_table.com_function(LONG, LONG, LONG, LONG)
    def setTimeouts(self, resolveTimeout: int, connectTimeout: int, sendTimeout: int, receiveTimeout: int) -> int:
        """
        Specify timeout settings (in milliseconds)
        """
    @virtual_table.com_function(VARIANT, PTR(BOOL))
    def waitForResponse(self, timeoutInSeconds: VARIANT, pOut: IPointer[BOOL]) -> int:
        """
        Wait for asynchronous send to complete, with optional timeout (in seconds)
        """
    @virtual_table.com_function(SERVERXMLHTTP_OPTION, PTR(VARIANT))
    def getOption(self, option: SERVERXMLHTTP_OPTION, pOut: IPointer[VARIANT]) -> int:
        """
        Get an option value
        """
    @virtual_table.com_function(SERVERXMLHTTP_OPTION, VARIANT)
    def setOption(self, option: SERVERXMLHTTP_OPTION, value: VARIANT) -> int:
        """
        Set an option value
        """
    virtual_table.build()

class IServerXMLHTTPRequest2(IDispatch):
    """
    IServerXMLHTTPRequest2 Interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{2E01311B-C322-4B0A-BD77-B90CFDC8DCE7}")

    @virtual_table.com_function(BSTR, BSTR, VARIANT, VARIANT, VARIANT)
    def open(self, bstrMethod: BSTR, bstrUrl: BSTR, varAsync: VARIANT, bstrUser: VARIANT, bstrPassword: VARIANT) -> int:
        """
        Open HTTP connection
        """
    @virtual_table.com_function(BSTR, BSTR)
    def setRequestHeader(self, bstrHeader: BSTR, bstrValue: BSTR) -> int:
        """
        Add HTTP request header
        """
    @virtual_table.com_function(BSTR, PTR(BSTR))
    def getResponseHeader(self, bstrHeader: BSTR, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP response header
        """
    @virtual_table.com_function(PTR(BSTR))
    def getAllResponseHeaders(self, pOut: IPointer[BSTR]) -> int:
        """
        Get all HTTP response headers
        """
    @virtual_table.com_function(VARIANT)
    def send(self, varBody: VARIANT) -> int:
        """
        Send HTTP request
        """
    @virtual_table.com_function()
    def abort(self) -> int:
        """
        Abort HTTP request
        """
    @virtual_table.com_function(PLONG)
    def get_status(self, pOut: IPointer[LONG]) -> int:
        """
        Get HTTP status code
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_statusText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get HTTP status text
        """
    @virtual_table.com_function(DOUBLE_PTR(IDispatch))
    def get_responseXML(self, ppOut: IDoublePtr[IDispatch]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(BSTR))
    def get_responseText(self, pOut: IPointer[BSTR]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseBody(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PTR(VARIANT))
    def get_responseStream(self, pOut: IPointer[VARIANT]) -> int:
        """
        Get response body
        """
    @virtual_table.com_function(PLONG)
    def get_readyState(self, pOut: IPointer[LONG]) -> int:
        """
        Get ready state
        """
    @virtual_table.com_function(PTR(IDispatch))
    def put_onreadystatechange(self, param0: IPointer[IDispatch]) -> int:
        """
        Register a complete event handler
        """
    @virtual_table.com_function(LONG, LONG, LONG, LONG)
    def setTimeouts(self, resolveTimeout: int, connectTimeout: int, sendTimeout: int, receiveTimeout: int) -> int:
        """
        Specify timeout settings (in milliseconds)
        """
    @virtual_table.com_function(VARIANT, PTR(BOOL))
    def waitForResponse(self, timeoutInSeconds: VARIANT, pOut: IPointer[BOOL]) -> int:
        """
        Wait for asynchronous send to complete, with optional timeout (in seconds)
        """
    @virtual_table.com_function(SERVERXMLHTTP_OPTION, PTR(VARIANT))
    def getOption(self, option: SERVERXMLHTTP_OPTION, pOut: IPointer[VARIANT]) -> int:
        """
        Get an option value
        """
    @virtual_table.com_function(SERVERXMLHTTP_OPTION, VARIANT)
    def setOption(self, option: SERVERXMLHTTP_OPTION, value: VARIANT) -> int:
        """
        Set an option value
        """
    @virtual_table.com_function(SXH_PROXY_SETTING, VARIANT, VARIANT)
    def setProxy(self, proxySetting: SXH_PROXY_SETTING, varProxyServer: VARIANT, varBypassList: VARIANT) -> int:
        """
        Specify proxy configuration
        """
    @virtual_table.com_function(BSTR, BSTR)
    def setProxyCredentials(self, bstrUserName: BSTR, bstrPassword: BSTR) -> int:
        """
        Specify proxy authentication credentials
        """
    virtual_table.build()

class IMXNamespacePrefixes(IDispatch):
    """
    IMXNamespacePrefixes interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{C90352F4-643C-4FBC-BB23-E996EB2D51FD}")

    @virtual_table.com_function(LONG, PTR(BSTR))
    def get_item(self, index: int, pOut: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(PLONG)
    def get_length(self, pOut: IPointer[LONG]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def get__newEnum(self, ppOut: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

class IVBMXNamespaceManager(IDispatch):
    """
    IVBMXNamespaceManager interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID("{C90352F5-643C-4FBC-BB23-E996EB2D51FD}")

    @virtual_table.com_function(BOOL)
    def put_allowOverride(self, param0: bool) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def get_allowOverride(self, pOut: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function()
    def reset(self) -> int: ...

    @virtual_table.com_function()
    def pushContext(self) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), BOOL)
    def pushNodeContext(self, contextNode: IPointer[IXMLDOMNode], fDeep: bool) -> int: ...

    @virtual_table.com_function()
    def popContext(self) -> int: ...

    @virtual_table.com_function(BSTR, BSTR)
    def declarePrefix(self, prefix: BSTR, namespaceURI: BSTR) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IMXNamespacePrefixes))
    def getDeclaredPrefixes(self, ppOut: IDoublePtr[IMXNamespacePrefixes]) -> int: ...

    @virtual_table.com_function(BSTR, DOUBLE_PTR(IMXNamespacePrefixes))
    def getPrefixes(self, namespaceURI: BSTR, ppOut: IDoublePtr[IMXNamespacePrefixes]) -> int: ...

    @virtual_table.com_function(BSTR, PTR(VARIANT))
    def getURI(self, prefix: BSTR, pOut: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(BSTR, PTR(IXMLDOMNode), PTR(VARIANT))
    def getURIFromNode(self, strPrefix: BSTR, contextNode: IPointer[IXMLDOMNode], pOut: IPointer[VARIANT]) -> int: ...

    virtual_table.build()

class IMXNamespaceManager(IUnknown):
    """
    IMXNamespaceManager interface
    """
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{C90352F6-643C-4FBC-BB23-E996EB2D51FD}")

    @virtual_table.com_function(BOOL)
    def putAllowOverride(self, fOverride: bool) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def getAllowOverride(self, fOverride: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function()
    def reset(self) -> int: ...

    @virtual_table.com_function()
    def pushContext(self) -> int: ...

    @virtual_table.com_function(PTR(IXMLDOMNode), BOOL)
    def pushNodeContext(self, contextNode: IPointer[IXMLDOMNode], fDeep: bool) -> int: ...

    @virtual_table.com_function()
    def popContext(self) -> int: ...

    @virtual_table.com_function(LPWSTR, LPWSTR)
    def declarePrefix(self, prefix: LPWSTR, namespaceURI: LPWSTR) -> int: ...

    @virtual_table.com_function(LONG, PWORD, PINT)
    def getDeclaredPrefix(self, nIndex: int, pwchPrefix: IPointer[WORD], pcchPrefix: IPointer[INT]) -> int: ...

    @virtual_table.com_function(LPWSTR, LONG, PWORD, PINT)
    def getPrefix(self, pwszNamespaceURI: LPWSTR, nIndex: int, pwchPrefix: IPointer[WORD], pcchPrefix: IPointer[INT]) -> int: ...

    @virtual_table.com_function(LPWSTR, PTR(IXMLDOMNode), PWORD, PINT)
    def getURI(self, pwchPrefix: LPWSTR, pContextNode: IPointer[IXMLDOMNode], pwchUri: IPointer[WORD], pcchUri: IPointer[INT]) -> int: ...

    virtual_table.build()

class DOMDocument(COMClass):
    """
W3C-DOM XML Document (Apartment)        """
    _clsid_ = CLSID("{F6D90F11-9C73-11D3-B32E-00C04F990BB4}")

class DOMDocument26(COMClass):
    """
W3C-DOM XML Document (Apartment)        """
    _clsid_ = CLSID("{F5078F1B-C551-11D3-89B9-0000F81FE221}")

class DOMDocument30(COMClass):
    """
W3C-DOM XML Document (Apartment)        """
    _clsid_ = CLSID("{F5078F32-C551-11D3-89B9-0000F81FE221}")

class FreeThreadedDOMDocument(COMClass):
    """
W3C-DOM XML Document (Free threaded)        """
    _clsid_ = CLSID("{F6D90F12-9C73-11D3-B32E-00C04F990BB4}")

class FreeThreadedDOMDocument26(COMClass):
    """
W3C-DOM XML Document (Free threaded)        """
    _clsid_ = CLSID("{F5078F1C-C551-11D3-89B9-0000F81FE221}")

class FreeThreadedDOMDocument30(COMClass):
    """
W3C-DOM XML Document (Free threaded)        """
    _clsid_ = CLSID("{F5078F33-C551-11D3-89B9-0000F81FE221}")

class XMLSchemaCache(COMClass):
    """
XML Schema Cache        """
    _clsid_ = CLSID("{373984C9-B845-449B-91E7-45AC83036ADE}")

class XMLSchemaCache26(COMClass):
    """
XML Schema Cache 2.6        """
    _clsid_ = CLSID("{F5078F1D-C551-11D3-89B9-0000F81FE221}")

class XMLSchemaCache30(COMClass):
    """
XML Schema Cache 3.0        """
    _clsid_ = CLSID("{F5078F34-C551-11D3-89B9-0000F81FE221}")

class XSLTemplate(COMClass):
    """
Compiled XSL Stylesheet Cache        """
    _clsid_ = CLSID("{2933BF94-7B36-11D2-B20E-00C04F983E60}")

class XSLTemplate26(COMClass):
    """
Compiled XSL Stylesheet Cache 2.6        """
    _clsid_ = CLSID("{F5078F21-C551-11D3-89B9-0000F81FE221}")

class XSLTemplate30(COMClass):
    """
Compiled XSL Stylesheet Cache 3.0        """
    _clsid_ = CLSID("{F5078F36-C551-11D3-89B9-0000F81FE221}")

class DSOControl(COMClass):
    """
XML Data Source Object        """
    _clsid_ = CLSID("{F6D90F14-9C73-11D3-B32E-00C04F990BB4}")

class DSOControl26(COMClass):
    """
XML Data Source Object        """
    _clsid_ = CLSID("{F5078F1F-C551-11D3-89B9-0000F81FE221}")

class DSOControl30(COMClass):
    """
XML Data Source Object        """
    _clsid_ = CLSID("{F5078F39-C551-11D3-89B9-0000F81FE221}")

class XMLHTTP(COMClass):
    """
XML HTTP Request class.        """
    _clsid_ = CLSID("{F6D90F16-9C73-11D3-B32E-00C04F990BB4}")

class XMLHTTP26(COMClass):
    """
XML HTTP Request class.        """
    _clsid_ = CLSID("{F5078F1E-C551-11D3-89B9-0000F81FE221}")

class XMLHTTP30(COMClass):
    """
XML HTTP Request class.        """
    _clsid_ = CLSID("{F5078F35-C551-11D3-89B9-0000F81FE221}")

class ServerXMLHTTP(COMClass):
    """
Server XML HTTP Request class.        """
    _clsid_ = CLSID("{AFBA6B42-5692-48EA-8141-DC517DCF0EF1}")

class ServerXMLHTTP30(COMClass):
    """
Server XML HTTP Request class.        """
    _clsid_ = CLSID("{AFB40FFD-B609-40A3-9828-F88BBE11E4E3}")

class SAXXMLReader(COMClass):
    """
SAX XML Reader (version independent) coclass        """
    _clsid_ = CLSID("{079AA557-4A18-424A-8EEE-E39F0A8D41B9}")

class SAXXMLReader30(COMClass):
    """
SAX XML Reader 3.0 coclass        """
    _clsid_ = CLSID("{3124C396-FB13-4836-A6AD-1317F1713688}")

class MXXMLWriter(COMClass):
    """
Microsoft XML Writer (version independent) coclass        """
    _clsid_ = CLSID("{FC220AD8-A72A-4EE8-926E-0B7AD152A020}")

class MXXMLWriter30(COMClass):
    """
Microsoft XML Writer 3.0 coclass        """
    _clsid_ = CLSID("{3D813DFE-6C91-4A4E-8F41-04346A841D9C}")

class MXHTMLWriter(COMClass):
    """
Microsoft HTML Writer (version independent) coclass        """
    _clsid_ = CLSID("{A4C23EC3-6B70-4466-9127-550077239978}")

class MXHTMLWriter30(COMClass):
    """
Microsoft HTML Writer 3.0 coclass        """
    _clsid_ = CLSID("{853D1540-C1A7-4AA9-A226-4D3BD301146D}")

class SAXAttributes(COMClass):
    """
SAX Attributes (version independent) coclass        """
    _clsid_ = CLSID("{4DD441AD-526D-4A77-9F1B-9841ED802FB0}")

class SAXAttributes30(COMClass):
    """
SAX Attributes 3.0 coclass        """
    _clsid_ = CLSID("{3E784A01-F3AE-4DC0-9354-9526B9370EBA}")

class MXNamespaceManager(COMClass):
    """
MX Namespace Manager coclass        """
    _clsid_ = CLSID("{88D969D5-F192-11D4-A65F-0040963251E5}")

class XMLDocument(COMClass):
    """
XMLDocument extends IXML Document.  It is obsolete.  You should use DOMDocument.  This object should not be confused with the XMLDocument property on the XML data island.        """
    _clsid_ = CLSID("{CFC399AF-D876-11D0-9C10-00C04FC99C8E}")

