DOMAINS = {
  "properties": {
    "domains": {
      "items": {
        "properties": {
          "logo_url": {
            "type": "string",
            "format": "url"
          },
          "is_excluded_from_feed": {
            "type": "boolean"
          },
          "is_readable_for_everyone": {
            "type": "boolean"
          },
          "name": {
            "attr_name": "name",
            "type": "string"
          },
          "title": {
            "attr_name": "title",
            "type": "string"
          },
          "url": {
            "type": "string",
            "format": "url"
          },
          "readers_count": {
            "type": "integer",
            "format": "int32"
          },
          "is_subscribed": {
            "type": "boolean"
          },
          "is_adult": {
            "type": "boolean"
          },
          "can_subscribe": {
            "type": "boolean"
          },
          "is_ignored": {
            "type": "boolean"
          },
          "color_schema": {
            "properties": {
              "irony_color": {
                "type": "string"
              },
              "links_system_color": {
                "type": "string"
              },
              "background_color": {
                "type": "string"
              },
              "header_color": {
                "type": "string"
              },
              "text_color": {
                "type": "string"
              }
            },
            "title": "Brief Domain Color Schema Response"
          },
          "prefix": {
            "type": "string"
          },
          "owner": {
            "properties": {
              "is_golden": {
                "type": "boolean"
              },
              "deleted": {
                "type": "boolean"
              },
              "gender": {
                "type": "string"
              },
              "rank": {
                "type": "string"
              },
              # "avatar_url": {
              #   "type": "string"
              # },
              "karma": {
                "type": "integer",
                "format": "int32"
              },
              "active": {
                "type": "boolean"
              },
              "login": {
                "type": "string"
              },
              # "rank_color": {
              #   "type": "string"
              # },
              "id": {
                "type": "integer",
                "format": "int32"
              }
            },
            "title": "User Response"
          },
          "president": {
            "properties": {
              "is_golden": {
                "type": "boolean"
              },
              "deleted": {
                "type": "boolean"
              },
              "gender": {
                "type": "string"
              },
              "rank": {
                "type": "string"
              },
              # "avatar_url": {
              #   "type": "string"
              # },
              "karma": {
                "type": "integer",
                "format": "int32"
              },
              "active": {
                "type": "boolean"
              },
              "login": {
                "type": "string"
              },
              # "rank_color": {
              #   "type": "string"
              # },
              "id": {
                "type": "integer",
                "format": "int32"
              }
            },
            "title": "User Response"
          },
          "is_elections_enabled": {
            "type": "boolean"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "description": {
            "attr_name": "description",
            "type": "string"
          }
        },
        "title": "Domain Response"
      },
      "type": "array"
    },
    "per_page": {
      "type": "integer",
      "format": "int32"
    },
    "page_count": {
      "type": "integer",
      "format": "int32"
    },
    "page": {
      "type": "integer",
      "format": "int32"
    },
    "item_count": {
      "type": "integer",
      "format": "int32"
    }
  },
  "title": "Domains Page Response"
}

POSTS = {
  "required": [
    "data"
  ],
  "properties": {
    "rating": {
      "type": "integer",
      "format": "int32"
    },
    "domain": {
      "properties": {
        "title": {
          "attr_name": "title",
          "type": "string"
        },
        "url": {
          "type": "string",
          "format": "url"
        },
        "readers_count": {
          "type": "integer",
          "format": "int32"
        },
        "is_subscribed": {
          "type": "boolean"
        },
        "is_ignored": {
          "type": "boolean"
        },
        "color_schema": {
          "properties": {
            "irony_color": {
              "type": "string"
            },
            "links_system_color": {
              "type": "string"
            },
            "background_color": {
              "type": "string"
            },
            "header_color": {
              "type": "string"
            },
            "text_color": {
              "type": "string"
            }
          },
          "title": "Brief Domain Color Schema Response"
        },
        "is_adult": {
          "type": "boolean"
        },
        "prefix": {
          "type": "string"
        },
        "logo_url": {
          "type": "string",
          "format": "url"
        },
        "id": {
          "type": "integer",
          "format": "int32"
        }
      },
      "title": "Simple Domain Response"
    },
    "unread_comments_count": {
      "type": "integer",
      "format": "int32"
    },
    "country_code": {
      "type": "string"
    },
    "in_favourites": {
      "type": "boolean"
    },
    "title": {
      "type": "string"
    },
    "can_unpublish": {
      "type": "boolean"
    },
    "golden": {
      "type": "boolean"
    },
    "id": {
      "type": "integer",
      "format": "int32"
    },
    "pinned": {
      "type": "boolean"
    },
    "user_vote": {
      "type": "integer",
      "format": "int32"
    },
    "can_ban": {
      "type": "boolean"
    },
    "_links": {
      "items": {
        "required": [
          "href",
          "method",
          "rel"
        ],
        "properties": {
          "href": {
            "type": "string"
          },
          "params": {
            "type": "string"
          },
          "method": {
            "type": "string"
          },
          "rel": {
            "type": "string"
          }
        },
        "title": "Hyper Link Response"
      },
      "type": "array"
    },
    "url_slug": {
      "type": "string"
    },
    "tags": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "main_image_url": {
      "type": "string"
    },
    "can_moderate": {
      "type": "boolean"
    },
    "hidden_rating_time_to_show": {
      "type": "integer",
      "description": "Timestamp when rating will be shown or Null if it's not hidden",
      "format": "int32"
    },
    "user": {
      "properties": {
        "is_golden": {
          "type": "boolean"
        },
        "deleted": {
          "type": "boolean"
        },
        "gender": {
          "type": "string"
        },
        "is_ignored": {
          "type": "boolean"
        },
        "rank": {
          "type": "string"
        },
        "avatar_url": {
          "type": "string"
        },
        "karma": {
          "type": "integer",
          "format": "int32"
        },
        "active": {
          "type": "boolean"
        },
        "login": {
          "type": "string"
        },
        "rank_color": {
          "type": "string"
        },
        "id": {
          "type": "integer",
          "format": "int32"
        }
      },
      "title": "Doc User Response"
    },
    "can_delete": {
      "type": "boolean"
    },
    "estimate": {
      "type": "integer",
      "format": "int32"
    },
    "data": {
      "oneOf": [
        {
          "required": [
            "title",
            "type"
          ],
          "properties": {
            "title": {
              "type": "string"
            },
            "text": {
              "type": "string"
            },
            "render_type": {
              "enum": [
                "mini",
                "maxi",
                "midi"
              ],
              "type": "string"
            },
            "snippet": {
              "type": "string"
            },
            "link": {
              "oneOf": [
                {
                  "required": [
                    "url",
                    "type"
                  ],
                  "properties": {
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "video": {
                      "type": "string",
                      "format": "url"
                    },
                    "type": {
                      "enum": [
                        "image"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    },
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    },
                    "is_animated": {
                      "type": "boolean"
                    }
                  },
                  "title": "Link Image"
                },
                {
                  "required": [
                    "url",
                    "type"
                  ],
                  "properties": {
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    },
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "height": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "width": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "embed": {
                      "required": [
                        "provider",
                        "id"
                      ],
                      "properties": {
                        "description": {
                          "type": "string"
                        },
                        "title": {
                          "type": "string"
                        },
                        "start_time": {
                          "type": "integer",
                          "description": "Время с которого начивать проигрывать в секундах",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "provider": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "date_uploaded": {
                          "type": "string"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Embed"
                    },
                    "type": {
                      "enum": [
                        "embed"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    }
                  },
                  "title": "Link Embed"
                },
                {
                  "required": [
                    "url",
                    "type"
                  ],
                  "properties": {
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "info": {
                      "type": "string"
                    },
                    "type": {
                      "enum": [
                        "web"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    },
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    }
                  },
                  "title": "Link Web"
                },
                {
                  "required": [
                    "url",
                    "type"
                  ],
                  "properties": {
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    },
                    "format": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "height": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "width": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "type": {
                      "enum": [
                        "video"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    }
                  },
                  "title": "Link Video"
                }
              ],
              "type": "object"
            },
            "media": {
              "required": [
                "url",
                "type"
              ],
              "properties": {
                "thumbnails": {
                  "properties": {
                    "width_120": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "original": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_500": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_330": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_700": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    }
                  },
                  "title": "Thumbnails"
                },
                "url": {
                  "type": "string",
                  "format": "url"
                },
                "height": {
                  "type": "integer",
                  "format": "int32"
                },
                "width": {
                  "type": "integer",
                  "format": "int32"
                },
                "video": {
                  "type": "string",
                  "format": "url"
                },
                "type": {
                  "enum": [
                    "image"
                  ],
                  "type": "string",
                  "format": "Constant string"
                },
                "is_animated": {
                  "type": "boolean"
                }
              },
              "title": "Media"
            },
            "type": {
              "enum": [
                "link"
              ],
              "type": "string",
              "format": "Constant string"
            }
          },
          "title": "Link Post Data"
        },
        {
          "required": [
            "blocks",
            "title",
            "type"
          ],
          "properties": {
            "blocks": {
              "oneOf": [
                {
                  "required": [
                    "text",
                    "type"
                  ],
                  "properties": {
                    "text": {
                      "type": "string"
                    },
                    "type": {
                      "enum": [
                        "text"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    }
                  },
                  "title": "Text Block"
                },
                {
                  "required": [
                    "url",
                    "align",
                    "type"
                  ],
                  "properties": {
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "align": {
                      "enum": [
                        "right",
                        "center",
                        "left"
                      ],
                      "type": "string"
                    },
                    "type": {
                      "enum": [
                        "embed"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    },
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    },
                    "embed": {
                      "required": [
                        "provider",
                        "id"
                      ],
                      "properties": {
                        "description": {
                          "type": "string"
                        },
                        "title": {
                          "type": "string"
                        },
                        "start_time": {
                          "type": "integer",
                          "description": "Время с которого начивать проигрывать в секундах",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "provider": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "date_uploaded": {
                          "type": "string"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Embed"
                    }
                  },
                  "title": "Embed Block"
                },
                {
                  "required": [
                    "url",
                    "align",
                    "type"
                  ],
                  "properties": {
                    "thumbnails": {
                      "properties": {
                        "width_120": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "original": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_500": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_330": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        },
                        "width_700": {
                          "required": [
                            "url"
                          ],
                          "properties": {
                            "url": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "is_animated": {
                              "type": "boolean"
                            }
                          },
                          "title": "Image"
                        }
                      },
                      "title": "Thumbnails"
                    },
                    "url": {
                      "type": "string",
                      "format": "url"
                    },
                    "text": {
                      "type": "string"
                    },
                    "align": {
                      "enum": [
                        "right",
                        "center",
                        "full",
                        "left"
                      ],
                      "type": "string"
                    },
                    "height": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "width": {
                      "type": "integer",
                      "format": "int32"
                    },
                    "video": {
                      "type": "string",
                      "format": "url"
                    },
                    "type": {
                      "enum": [
                        "image"
                      ],
                      "type": "string",
                      "format": "Constant string"
                    },
                    "is_animated": {
                      "type": "boolean"
                    }
                  },
                  "title": "Image Block"
                }
              ],
              "type": "array"
            },
            "title": {
              "type": "string"
            },
            "header_color": {
              "enum": [
                "white",
                "black"
              ],
              "type": "string"
            },
            "snippet": {
              "type": "string"
            },
            "cover_image": {
              "required": [
                "url"
              ],
              "properties": {
                "url": {
                  "type": "string",
                  "format": "url"
                },
                "width": {
                  "type": "integer",
                  "format": "int32"
                },
                "is_animated": {
                  "type": "boolean"
                },
                "thumbnails": {
                  "properties": {
                    "width_120": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "original": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_500": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_330": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_700": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    }
                  },
                  "title": "Thumbnails"
                },
                "height": {
                  "type": "integer",
                  "format": "int32"
                }
              },
              "title": "Cover Image"
            },
            "subtitle": {
              "type": "string"
            },
            "type": {
              "enum": [
                "article"
              ],
              "type": "string",
              "format": "Constant string"
            },
            "preview_image": {
              "required": [
                "url"
              ],
              "properties": {
                "url": {
                  "type": "string",
                  "format": "url"
                },
                "width": {
                  "type": "integer",
                  "format": "int32"
                },
                "is_animated": {
                  "type": "boolean"
                },
                "thumbnails": {
                  "properties": {
                    "width_120": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "original": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_500": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_330": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_700": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    }
                  },
                  "title": "Thumbnails"
                },
                "height": {
                  "type": "integer",
                  "format": "int32"
                }
              },
              "title": "Cover Image"
            }
          },
          "title": "Article Post Data"
        },
        {
          "required": [
            "type",
            "gallery",
            "title"
          ],
          "properties": {
            "text": {
              "type": "string"
            },
            "type": {
              "enum": [
                "gallery"
              ],
              "type": "string",
              "format": "Constant string"
            },
            "gallery": {
              "items": {
                "required": [
                  "url",
                  "type"
                ],
                "properties": {
                  "thumbnails": {
                    "properties": {
                      "width_120": {
                        "required": [
                          "url"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Image"
                      },
                      "original": {
                        "required": [
                          "url"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Image"
                      },
                      "width_500": {
                        "required": [
                          "url"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Image"
                      },
                      "width_330": {
                        "required": [
                          "url"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Image"
                      },
                      "width_700": {
                        "required": [
                          "url"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Image"
                      }
                    },
                    "title": "Thumbnails"
                  },
                  "url": {
                    "type": "string",
                    "format": "url"
                  },
                  "text": {
                    "type": "string"
                  },
                  "height": {
                    "type": "integer",
                    "format": "int32"
                  },
                  "width": {
                    "type": "integer",
                    "format": "int32"
                  },
                  "type": {
                    "type": "string"
                  },
                  "is_animated": {
                    "type": "boolean"
                  }
                },
                "title": "Gallery Image"
              },
              "type": "array"
            },
            "subtitle": {
              "type": "string"
            },
            "title": {
              "type": "string"
            }
          },
          "title": "Gallery Post Data"
        },
        {
          "required": [
            "title",
            "type"
          ],
          "properties": {
            "online_expires_at": {
              "type": "integer",
              "format": "int32"
            },
            "contributors": {
              "items": {
                "properties": {
                  "is_golden": {
                    "type": "boolean"
                  },
                  "deleted": {
                    "type": "boolean"
                  },
                  "gender": {
                    "type": "string"
                  },
                  "rank": {
                    "type": "string"
                  },
                  "avatar_url": {
                    "type": "string"
                  },
                  "karma": {
                    "type": "integer",
                    "format": "int32"
                  },
                  "active": {
                    "type": "boolean"
                  },
                  "login": {
                    "type": "string"
                  },
                  "rank_color": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer",
                    "format": "int32"
                  }
                },
                "title": "Stream User Response"
              },
              "type": "array"
            },
            "title": {
              "type": "string"
            },
            "last_online_at": {
              "type": "integer",
              "format": "int32"
            },
            "text": {
              "type": "string"
            },
            "related_posts": {
              "items": {
                "required": [
                  "id"
                ],
                "properties": {
                  "url": {
                    "type": "string",
                    "format": "url"
                  },
                  "rating": {
                    "type": "integer",
                    "format": "int32"
                  },
                  "domain": {
                    "required": [
                      "id"
                    ],
                    "properties": {
                      "prefix": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer",
                        "format": "int32"
                      }
                    },
                    "title": "Domain"
                  },
                  "id": {
                    "type": "integer",
                    "format": "int32"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "title": "Related Post"
              },
              "type": "array"
            },
            "is_online": {
              "type": "boolean"
            },
            "type": {
              "enum": [
                "stream"
              ],
              "type": "string",
              "format": "Constant string"
            },
            "events": {
              "items": {
                "required": [
                  "blocks",
                  "user"
                ],
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "important": {
                    "type": "boolean"
                  },
                  "blocks": {
                    "oneOf": [
                      {
                        "required": [
                          "text",
                          "type"
                        ],
                        "properties": {
                          "text": {
                            "type": "string"
                          },
                          "type": {
                            "enum": [
                              "text"
                            ],
                            "type": "string",
                            "format": "Constant string"
                          }
                        },
                        "title": "Text Block"
                      },
                      {
                        "required": [
                          "url",
                          "align",
                          "type"
                        ],
                        "properties": {
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "align": {
                            "enum": [
                              "right",
                              "center",
                              "left"
                            ],
                            "type": "string"
                          },
                          "type": {
                            "enum": [
                              "embed"
                            ],
                            "type": "string",
                            "format": "Constant string"
                          },
                          "thumbnails": {
                            "properties": {
                              "width_120": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "original": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_500": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_330": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_700": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              }
                            },
                            "title": "Thumbnails"
                          },
                          "embed": {
                            "required": [
                              "provider",
                              "id"
                            ],
                            "properties": {
                              "description": {
                                "type": "string"
                              },
                              "title": {
                                "type": "string"
                              },
                              "start_time": {
                                "type": "integer",
                                "description": "Время с которого начивать проигрывать в секундах",
                                "format": "int32"
                              },
                              "height": {
                                "type": "integer",
                                "format": "int32"
                              },
                              "width": {
                                "type": "integer",
                                "format": "int32"
                              },
                              "provider": {
                                "type": "string"
                              },
                              "id": {
                                "type": "string"
                              },
                              "date_uploaded": {
                                "type": "string"
                              },
                              "is_animated": {
                                "type": "boolean"
                              }
                            },
                            "title": "Embed"
                          }
                        },
                        "title": "Embed Block"
                      },
                      {
                        "required": [
                          "url",
                          "type"
                        ],
                        "properties": {
                          "thumbnails": {
                            "properties": {
                              "width_120": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "original": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_500": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_330": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              },
                              "width_700": {
                                "required": [
                                  "url"
                                ],
                                "properties": {
                                  "url": {
                                    "type": "string",
                                    "format": "url"
                                  },
                                  "width": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "height": {
                                    "type": "integer",
                                    "format": "int32"
                                  },
                                  "is_animated": {
                                    "type": "boolean"
                                  }
                                },
                                "title": "Image"
                              }
                            },
                            "title": "Thumbnails"
                          },
                          "url": {
                            "type": "string",
                            "format": "url"
                          },
                          "height": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "width": {
                            "type": "integer",
                            "format": "int32"
                          },
                          "video": {
                            "type": "string",
                            "format": "url"
                          },
                          "type": {
                            "enum": [
                              "image"
                            ],
                            "type": "string",
                            "format": "Constant string"
                          },
                          "is_animated": {
                            "type": "boolean"
                          }
                        },
                        "title": "Event Image Block"
                      }
                    ],
                    "type": "array"
                  },
                  "user": {
                    "properties": {
                      "is_golden": {
                        "type": "boolean"
                      },
                      "deleted": {
                        "type": "boolean"
                      },
                      "gender": {
                        "type": "string"
                      },
                      "rank": {
                        "type": "string"
                      },
                      "avatar_url": {
                        "type": "string"
                      },
                      "karma": {
                        "type": "integer",
                        "format": "int32"
                      },
                      "active": {
                        "type": "boolean"
                      },
                      "login": {
                        "type": "string"
                      },
                      "rank_color": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer",
                        "format": "int32"
                      }
                    },
                    "title": "Stream User Response"
                  },
                  "created": {
                    "type": "integer",
                    "format": "int32"
                  }
                },
                "title": "Event"
              },
              "type": "array"
            }
          },
          "title": "Stream Post Data"
        },
        {
          "required": [
            "type",
            "title"
          ],
          "properties": {
            "image": {
              "required": [
                "url"
              ],
              "properties": {
                "url": {
                  "type": "string",
                  "format": "url"
                },
                "width": {
                  "type": "integer",
                  "format": "int32"
                },
                "thumbnails": {
                  "properties": {
                    "width_120": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "original": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_500": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_330": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    },
                    "width_700": {
                      "required": [
                        "url"
                      ],
                      "properties": {
                        "url": {
                          "type": "string",
                          "format": "url"
                        },
                        "width": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "height": {
                          "type": "integer",
                          "format": "int32"
                        },
                        "is_animated": {
                          "type": "boolean"
                        }
                      },
                      "title": "Image"
                    }
                  },
                  "title": "Thumbnails"
                },
                "height": {
                  "type": "integer",
                  "format": "int32"
                }
              },
              "title": "Comics Image"
            },
            "comics_source": {
              "required": [
                "bubbles",
                "grid"
              ],
              "properties": {
                "bubbles": {
                  "items": {
                    "required": [
                      "text",
                      "callout",
                      "font_size",
                      "anchor",
                      "position"
                    ],
                    "properties": {
                      "text": {
                        "type": "string"
                      },
                      "callout": {
                        "enum": [
                          "none",
                          "balls",
                          "arrow"
                        ],
                        "type": "string"
                      },
                      "font_size": {
                        "type": "number"
                      },
                      "anchor": {
                        "required": [
                          "y",
                          "x"
                        ],
                        "properties": {
                          "y": {
                            "type": "number"
                          },
                          "x": {
                            "type": "number"
                          }
                        },
                        "title": "Coordinates"
                      },
                      "position": {
                        "required": [
                          "y",
                          "x"
                        ],
                        "properties": {
                          "y": {
                            "type": "number"
                          },
                          "x": {
                            "type": "number"
                          }
                        },
                        "title": "Coordinates"
                      }
                    },
                    "title": "Bubble"
                  },
                  "type": "array"
                },
                "grid": {
                  "properties": {
                    "rows": {
                      "items": {
                        "items": {
                          "required": [
                            "src",
                            "height",
                            "width"
                          ],
                          "properties": {
                            "src": {
                              "type": "string",
                              "format": "url"
                            },
                            "width": {
                              "type": "integer",
                              "format": "int32"
                            },
                            "height": {
                              "type": "integer",
                              "format": "int32"
                            }
                          },
                          "title": "Row"
                        },
                        "type": "array"
                      },
                      "type": "array"
                    }
                  },
                  "title": "Grid"
                }
              },
              "title": "Comics"
            },
            "type": {
              "enum": [
                "comics"
              ],
              "type": "string",
              "format": "Constant string"
            },
            "title": {
              "type": "string"
            }
          },
          "title": "Comics Post Data"
        }
      ],
      "type": "object"
    },
    "in_interests": {
      "type": "boolean"
    },
    "can_edit": {
      "type": "boolean"
    },
    "favourites_count": {
      "type": "integer",
      "format": "int32"
    },
    "can_change_render_type": {
      "type": "boolean"
    },
    "created": {
      "type": "integer",
      "format": "int32"
    },
    "changed": {
      "type": "integer",
      "format": "int32"
    },
    "vote_weight": {
      "type": "integer",
      "format": "int32"
    },
    "comments_count": {
      "type": "integer",
      "format": "int32"
    },
    "advertising": {
      "type": "string"
    },
    "has_subscribed": {
      "type": "boolean",
      "description": "Подписан на пост"
    }
  },
  "title": "Post Response"
}